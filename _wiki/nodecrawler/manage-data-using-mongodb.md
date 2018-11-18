---
title: "Manage Data Using MongoDB"
excerpt: ""
date: 2018-07-18
toc: true
category:
- 'Node Crawler'
tag:
- 'Node'
- 'Crawler'
source:
- name: 03-保存数据到数据库@ninthakeey
  title: 'https://nintha.github.io/2018/07/08/Node%E7%88%AC%E8%99%AB%E6%8C%87%E5%8C%97/03-%E4%BF%9D%E5%AD%98%E6%95%B0%E6%8D%AE%E5%88%B0%E6%95%B0%E6%8D%AE%E5%BA%93/'
notify: 'The original Chinese article is written by ninthakeey. It has been translated and remixed by Datumorphism'
weight: 3
---


In most cases, databases makes the management of data quite convenient. In this article, we would scrape data using the code we discussed before but write data into MongoDB.

For installation of MongoDB, please refer to the [official documentation](https://docs.mongodb.com/manual/installation/).

## The Code

To write data to MongoDB using Node.js, we choose the package [`mongojs`](https://github.com/mafintosh/mongojs#readme), which provides almost exactly the standard MongoDB syntax.

To install `mongojs`,
```terminal
npm i mongojs --save
```

Here is a module that can write data to MongoDB. We create a file named `dao.js` and copy pase the following code into it.

```JavaScript
// use mongojs
const mongojs = require('mongojs')
// connect to the database 'simple_spider' in MongoDB and use collection 'test'
const localdb = mongojs('simple_spider', ['test'])
// a function that saves data to MongoDB
const saveData = (data,cb) => {
	localdb.test.save(data, (err, res)=>{
	 	cb && cb(err, res)
	})
}
// a function that prints out the data to console
const printAllData = (cb) => {
	localdb.test.find({},(err, docs)=>{
		console.log(docs)
		cb && cb(err, docs)
	})
}
// close connection to MongoDB in case of memory leak
const closeMongo = () => localdb.close()
// expose the functions in this module to the program
module.exports = {
	saveData,printAllData,closeMongo
}
```



<div class="card">
<header class="card-header">
<p class="card-header-title card-toggle"> () => </p>
</header>
<div class="card-content is-hidden">
<div class="content" markdown="1">
In Node.js, [arrow function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) is keystroke saver for function expressions. It comes without `this`, arguments, super, etc.

In the above code, the expression
```JavaScript
const printAllData = (cb) => {
  // ...
}
```
defines a function named `printAllData` with argument `cb` and does something as indicated inside the curly bracket.
</div>
</div>
</div>


Three functions are provided in this module, `saveData`, `printAllData` and `closeMongo`. We will grab our previous code and call the functions from this module. We would like to modify the `index.js` file to make it look like the following.

```JavaScript
const superagent = require('superagent')
const fs = require('fs')
const dao = require('./dao')
superagent
	.get('https://api.bilibili.com/x/web-interface/archive/stat')
	.query({ aid:26763233 })
	.then(res => {
    // obtain the data to be saved
		const data = res.body.data
		dao.saveData(data, (err,res)=>{
			console.log('saved data')
			// save data to MongoDB and close connection
			dao.printAllData( () => dao.closeMongo() )
		})
	})
	.catch(err => console.error(err))
```

Run the code with the command
```terminal
node index
```
and we obtaint he following output:
```terminal
saved data
[ { _id: 5b41d634f3df89032c834d5b,
    aid: 26186448,
    view: 619751,
    danmaku: 12053,
    reply: 3500,
    favorite: 14961,
    coin: 40699,
    share: 1676,
    like: 20751,
    now_rank: 0,
    his_rank: 1,
    no_reprint: 1,
    copyright: 1 } ]
```
With this print out, we would have already have out data stored in our MongoDB.
