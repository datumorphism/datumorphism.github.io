---
title: "Basic Node Crawler"
excerpt: ""
date: 2018-07-15
toc: true
category:
- 'Node Crawler'
tag:
- 'Node'
- 'Crawler'
source:
- name: 02-实现一个简单的爬虫@ninthakeey
  link: 'https://nintha.github.io/2018/07/08/Node%E7%88%AC%E8%99%AB%E6%8C%87%E5%8C%97/02-%E5%AE%9E%E7%8E%B0%E4%B8%80%E4%B8%AA%E7%AE%80%E5%8D%95%E7%9A%84%E7%88%AC%E8%99%AB/'
notify: 'The original Chinese article is written by ninthakeey. It has been translated and remixed by Datumorphism'
weight: 2
---


## Prerequisites

1. Nodejs >= 8.9

## Overview

A model for a crawler is as follows.

A crawler requests data from the server, while the server responds with some data. Here is a graphic illustration

```
+----------+                +-----------+
|          |  HTTP Request  |           |
|          +---------------->           |
|  Nodejs  |                |  Servers  |
|          <----------------+           |
|          |  HTTP Response |           |
+----------+                +-----------+
```


<div class="card">
	<header class="card-header">
		<p class="card-header-title card-toggle">HTTP Requests</p>
	</header>
	<div class="card-content is-hidden">
		<div class="content">
			For a good introduction of HTTP requests, please refer to this video on youtube: <a href="https://www.youtube.com/watch?v=po3zYOe00O4">Explained HTTP, HTTPS, SSL/TLS</a>

      <iframe width="560" height="315" src="https://www.youtube.com/embed/po3zYOe00O4" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

		</div>
	</div>
</div>

## API

As for the first step, we need to find which url to request. Chrome and Firefox based browsers come with the developer's tool.

In this tutorial, we will be using bilibili.com as an example, which is a video hosting website in China. Bilibili hosts many videos. Along with each video, the status such as the number of viewers of the videos is also displayed. To find out which API we should use, we simple turn on Chrome dev tool, look in to the Network tab and find it among the XHR.

<div class="card">
	<header class="card-header">
		<p class="card-header-title card-toggle">screenshot of an example page</p>
	</header>
	<div class="card-content is-hidden">
		<div class="content">
    <img src="../assets/chrome-dev-tool-for-api.jpg"/>
		</div>
	</div>
</div>

One we obtained the API, we should start coding.

## The Code

All we need to do is to request from `https://api.bilibili.com/x/web-interface/archive/stat?aid=26763233` and display the data.

We will use the package [`superagent`](https://visionmedia.github.io/superagent/) to send HTTP requests.

<div class="card">
	<header class="card-header">
		<p class="card-header-title card-toggle">superagent</p>
	</header>
	<div class="card-content is-hidden">
		<div class="content">
			'superagent' is a lightweight node package for ajax API.
		</div>
	</div>
</div>

For a first taste of the code, we will run everything on repl.it. Please hit the button on the bottom right corner of the following embed environment to run the code. The code can also be modified as you wish. The results shown in the terminal contains the returned data which is in JSON format as usual.

<iframe height="400px" width="100%" src="https://repl.it/@emptymalei/crawler-demo-bili?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

There is absolute no magic here. The annotated code is provided.
{% highlight JavaScript %}
// we use superagent to request from server
const superagent = require('superagent')
superagent
  // send GET requests to url
	.get('https://api.bilibili.com/x/web-interface/archive/stat')
  // here goes the parameters for the request
  // we could also use https://api.bilibili.com/x/web-interface/archive/stat?aid=26763233
  // as the get url and leave this query function no arguments
  // query function will take the dict of parameters
  // and append the to the url as ?aid=26763233
	.query({ aid:26763233 })
  // excute console.log() if the response is successfull
  // console.log() prints the results in the terminal
	.then(res => res && console.log(res.body))
  // catch error and print it in terminal if it fails
	.catch(err => console.error(err))
{% endhighlight %}

## Local Manipulation

However, we should not run a production crawler on repl.it. It is the best practice to set up your local programming environment according to the previous article of this series and program on your own computer.

First of all, we create a folder `node-simple-spider` (or whatever you like) to contain all the files. To install the dependency `superagent`, we open a terminal and go to this folder. Inside this folder, we type in the terminal
```terminal
npm i superagent --save
```
<div class="card">
	<header class="card-header">
		<p class="card-header-title card-toggle">npm and node packages</p>
	</header>
	<div class="card-content is-hidden">
		<div class="content">
			'npm' is the node package manager. The command we typed in will install the package 'superagent' inside this folder.
		</div>
	</div>
</div>

We create a file with the name `index.js` in the folder. We copy and paste the following code to the file.
{% highlight JavaScript %}
const superagent = require('superagent')

superagent
	.get('https://api.bilibili.com/x/web-interface/archive/stat')
	.query({aid:26763233})
	.then(res => res && console.log(res.body))
	.catch(err => console.error(err))
{% endhighlight %}

To run the code, use
```terminal
node index.js
```
in the terminal. The result will be printed in the terminal as follows:
```terminal
{ code: 0,
  message: '0',
  ttl: 1,
  data:
   { aid: 26763233,
     view: 113830,
     danmaku: 757,
     reply: 260,
     favorite: 12947,
     coin: 2859,
     share: 228,
     like: 1833,
     now_rank: 0,
     his_rank: 47,
     no_reprint: 1,
     copyright: 1 }
}
```


## Dump Data to File

We can barely do anything with the data if the program only prints it in the terminal. To analyze the data, one simple solution is to save the data in a file.

Node.js comes with a package `fs` which can be used to save data to a file. The code to achieve this is:
{% highlight JavaScript %}
const superagent = require('superagent')
// fs is a standard package that comes with Node.js
const fs = require('fs')
superagent
	.get('https://api.bilibili.com/x/web-interface/archive/stat')
	.query({ aid:26763233 })
		// dump data in a JSON file
	.then(res => {
		try{
			fs.writeFile('data.json', res.text, err => {
  				console.log('The data is written to data.json!');
			});
		} catch(err) {
			console.error(err)
		}
	})
	.catch(err => console.error(err))
{% endhighlight %}

We run the code in the terminal. The code will generate a data file `data.json` in the same folder.

`fs.writeFile` will generate the file with each run. A file with the same name will be overwritten. To append data to a file, simply replace `fs.writeFile` with `fs.appendFile`.
{: .notes--primary}

<div class="card">
<header class="card-header">
<p class="card-header-title card-toggle">Non-blocking I/O</p>
</header>
<div class="card-content is-hidden">
<div class="content" markdown="1">
The function `fs.writeFile()` performs the I/O asynchronously. The next line of code runs without waiting for the I/O to finish. This is different from Python. We will explain and explore more asynchronous feature in the future.
</div>
</div>
</div>



## Useful Links

1. [SuperAgent](https://www.npmjs.com/package/superagent)
