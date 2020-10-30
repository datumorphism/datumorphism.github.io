---
title: "Restrictions of Websites"
date: 2018-07-19
category:
- 'Node Crawler'
tags:
- 'Node'
- 'Crawler'
references:
- name: 04-应对网站的限制@ninthakeey
  link: 'https://nintha.github.io/2018/07/08/node_spider_compass/04-against_website_limitation/'
- name: "Node.JS Concurrency with Async/Await and Promises!"
  link: https://medium.com/platformer-blog/node-js-concurrency-with-async-await-and-promises-b4c4ae8f4510
notify: 'The original Chinese article is written by [ninthakeey](https://github.com/nintha). It has been translated and remixed by Datumorphism'
weight: 4
---

Beware that scraping data off websites is neither always allowed nor as easy as a few lines of code. The preceding articles enable you to scrape many data, however, man websites have counter measures. In this article, we will be dealing with some of the common ones.


## Request Frequency

Some websites have limitations on the frequency of API requests. The solution to this is simply a brief pause after each request. In Node.js, the function [`setInterval`](https://www.w3schools.com/jsref/met_win_setinterval.asp) enables this.

```JavaScript
// ... require packages here

// define the function fetch to get data
const fetch = (aid) => superagent
		.get('https://api.bilibili.com/x/web-interface/archive/stat')
		.query({ aid:aid })
		.then(res => {
			const data = res.body.data
			dao.saveData(data, (err,res)=>{
				console.log('saved data, aid=' + aid)
			})
		})
		.catch(err => console.error(err))
// fetch data for every 2000ms
// increment aid to scrape other aid's
let aid = 26186448
setInterval(() => fetch(aid++), 2000)
```

{{< card title="setInterval" >}}

`setInterval` is used as
```JavaScript
setInterval(function(){ alert("Hello"); }, 3000);
```
The function inside is a callback function.

As mentioned previously, `() => ` defines a function. In our case, we have called the function `fetch` increment `aid` using `aid++`.
{{</card>}}


Node.js provides other approaches such as the new ES8 syntax `async/await` which make it possible to rewrite the code into function chaining again.
```JavaScript
// create a new Promise object
const sleep = (ms) => new Promise((suc,fail) => setTimeout(suc, ms));
(async ()=>{
	for(;;){
		await sleep(2000)
		console.log(new Date())
	}
})()
```
This piece of code will print out the date and time every 2000ms.

{{< card title="async/await">}}

Node.js is single-threaded. As we have mentioned when explaining the function `fs.writeFile()`, Node.js has non-blocking I/O. In fact, concurrency is probably at the heart of Node.js, which means we execute one process out of the multiple running processes. Concurrency can make your code more efficient.

In the first block of code, we have used `setInterval` callback function. However, the callback is kind of messy. It's much better if we could use function chaining. `Promise` is exactly what we need to achieve this.

`async` tells Node.js that we are defining an asynchronous function, while `await` tells it to wait for the async function to parse things. It's basically an alternative to `.then` and `.catch` functions.

The code above doesn't chain functions a lot but it's worth mentioning here.

[This article](https://medium.com/platformer-blog/node-js-concurrency-with-async-await-and-promises-b4c4ae8f4510) explains the concurrency in Node.js pretty well.
{{</card>}}


## User-Agent Verification

Some services will require some certain browsers to get a successful response. The way they do it is to verify the `User-Agent` (UA) data in the HTTP requests. In this case, we have to request with some fake UA data.

The package `superagent` can help us set UA.
```JavaScript
superagent
	.get('https://api.bilibili.com/x/web-interface/archive/stat')
	.set({ 'User-Agent': 'Opera/9.80 balabala...' }) // set User-Agent here
	.query({ aid:aid })
	.then(res => {
		// do something
	})
	.catch(err => console.error(err))
```

It would be even better if we could change UA everytime. Here is a list of UA.

```JavaScript
const USER_AGENTS = [
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0) ,Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre',
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',
    'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
    'Opera/9.25 (Windows NT 5.1; U; en), Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
];
```
