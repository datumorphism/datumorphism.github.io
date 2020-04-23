---
title: "Optimization"
excerpt: ""
date: 2018-07-19
toc: true
category:
- 'Node Crawler'
tag:
- 'Node'
- 'Crawler'
source:
- name: 05-微小的优化@ninthakeey
  link: 'https://nintha.github.io/2018/07/10/Node%E7%88%AC%E8%99%AB%E6%8C%87%E5%8C%97/05-%E5%BE%AE%E5%B0%8F%E7%9A%84%E4%BC%98%E5%8C%96/'
notify: 'The original Chinese article is written by ninthakeey. It has been translated and remixed by Datumorphism'
weight: 5
---

In this article, we will be optimizing the crawler to get better performance.

## Batch Jobs

In the article about using MongoDB as data storage, we write the data to database whenever we get it. In practice, this is not efficient at all. Here comes the batch jobs. It would be much better if one write to database with batch jobs.

If you recall, the code we used to write to database is
```JavaScript
// ...other code
localdb.test.save(data, (err, res)=>{
	// do something
})
```
The function `save` takes in not only one entry of document but an array of documents:
```JavaScript
const array = []
for(let i = INI_ID ; i < MAX_ID; i++){
	// fetch data from website
	const data =  fetchData(i)
    array.push(data)
}
localdb.test.save(array, (err, res)=>{
	// do something
})
```
It's essentially the same code but it helps with the efficiency.

## Asynchronous and Synchronous

Data scraping can be either asynchronous or synchronous.

Synchronous code is easier to read and debug. However, blocking of one function slows down the whole program.
```JavaScript
const main = async (MAX_ID) => {
    const array = []
    for(let i = 0 ; i < MAX_ID; i++){
        // fetch data from website
        const data = await fetchData(i) //this return a Promise
        array.push(data)
    }
    saveToMongoDB(array);
}
main(1000);
```


Asynchronous code solves the blocking problem but introduces complexities. Since it doesn't stop the code from executing the following functions, each function requires a timeout limit.
```JavaScript
const main = async (MAX_ID) => {
    const array = []
    for(let i = 0 ; i < MAX_ID; i++){
        // fetch data from website
        fetchData(i) // it return a Promise
        	.then(data => array.push(data))
        await sleep(100) // block thread 100 ms
    }
    // wait for async threads
    while(array.length < MAX_ID){
        await sleep(100)
    }
    saveToMongoDB(array);
}
main(1000);
```


## Resume Jobs

For large sites, the data scraping time is incredibly long. Failure in power, windows update, or even a tiny unidentified bug in the code could interrupt the program. It is crucial to be able to resume the crawler from the last termination. Especially when the code is asynchronous, termination of the program may lead to broken data.

One of the solutions is to write some synchronous code and record the most recent data id which should be already in the database and resume from this if interruptions should occur. The problem is that we have not utilized the full power of Node.js if we insist on the synchronous code.

Basically, information about the latest run has to be recorded in order to resume the process. We will write all the data of a batch job to the database and secure it.

One of the solutions is to create a database collection in MongoDB, say `package`. In this collection, we store two fields, `pid` and `status`, where `pid` is the batch job id and `status` is the status of this batch job. For example, we define `0`, `1`, and `-1` of status to be 'waiting', 'finished', and 'running', respectively.

```text
0: waiting
1: finished
-1: running
```

Here is some useful functions.
```JavaScript
// obtain most batch job id of status waiting
const findOneWaitingPackage = async () => {
    return new Promise((resolve, reject) =>
        localdb.package
            .find({ status: { $lte: 0 } })
            .sort({
                status: -1,
                pid: 1
            })
            .limit(1, (err, doc) => {
                if (err) reject(err)
                else {
                    updatePackageToRunning(doc[0])
                    resolve(doc[0])
                }
            })
    )
}
// reset package collection in database
// create two fields: status and pid
const resetPackage = async () => {
    indexMember().catch(err => console.error(err))
    return new Promise((resolve, reject) =>
        localdb.package.drop(() => {
            localdb.package.ensureIndex({ status: 1 }, () => {
                localdb.package.ensureIndex(
                    { pid: 1 },
                    { unique: true },
                    (err, res) => (err ? reject(err) : resolve(res))
                )
            })
        })
    )
}

// create documents of batch jobs
// package status: 0-waiting, 1-finished，-1-running
const insertPackage = async (start, end) => {
    const packs = Array(end - start + 1)
        .fill(0)
        .map((v, i) => {
            return {
                pid: i + start,
                status: 0
            }
        })
    return new Promise((resolve, reject) =>
        localdb.package.insert(
            packs,
            (err, res) => (err ? reject(err) : resolve(res && res.length))
        )
    )
}
// update batch job status to running
const updatePackageToRunning = async pid => {
    if (!pid) return
    return new Promise((resolve, reject) =>
        localdb.package.update(
            { pid },
            { $set: { status: -1 } },
            { multi: false },
            (err, doc) => (err ? reject(err) : resolve(doc))
        )
    )
}
// update batch job id to finished
const updatePackageToFinished = async pid => {
    return new Promise((resolve, reject) =>
        localdb.package.update(
            { pid },
            { $set: { status: 1 } },
            { multi: false },
            (err, doc) => (err ? reject(err) : resolve(doc))
        )
    )
}
```

The functions `resetPackage` and `insertPackage` will be executed on the first run. They will create a collection with all the batch job ids.

The function `findOneWaitingPackage` will obtain one of the batch jobs. `updatePackageToRunning` will change the status to finished whenever the batch job is done. `findOneWaitingPackage` will return the value `null` when it can not find any document with status `0`, which can be used to end the program.
