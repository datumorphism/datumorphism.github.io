---
title: "Basics of Network"
excerpt: "Essential knowledge of internet"
date: 2018-09-23
toc: true
category:
- 'Computation'
tag:
- 'Internet'
- 'Basics'
notify: 'I am transitioning from a physicist to a data scientist. While I am exploring the world of data, I find that I need to know some basics about computers and internet.'
weight: 3
---

## HTTP Keywords

1. Hyper Text Transfer Protocal: deliver hyper text from server to local browser etc.
2. Based on TCP/IP
3. Current version:  HTTP/2
4. Server  - Client
5. Client can request through GET, HEAD, POST, PUT, DELETE, TRACE, OPTIONS, CONNECT, PATCH.
6. Transfer anything defined by Content-Type
7. Connectionless Protocol: doesn't maintain the connection all the time
8. Stateless protocal: [A very nice explanation](https://www.zhihu.com/question/23202402/answer/300614865)



## URL Keywords

1. Uniform Resource Locator
2. Interpret each part of this URL: http://abc.com:8000/folder/file.html#title1location?param1=123&param2=234
9. No limits on length of URL by HTTP itself. However, some servers or clients do set limits.

Difference between URI and URL and URN: [The Difference Between URLs and URIs](https://danielmiessler.com/study/url-uri/) checkout the Venn diagram.

![](../assets/URI-vs-URL.png)

*From [The Difference Between URLs and URIs](https://danielmiessler.com/study/url-uri/)*


## How HTTP Works

HTTP Request: use Chrome Dev Tool -> Network to find out the requests, including GET and Response.


<div style="position: relative; padding-bottom: 1em; height: 0; overflow: hidden; max-width: 100%; height: auto;">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/po3zYOe00O4" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
</div>


### How to Request

1. `GET`: request for the page 
2. `HEAD`: similar to `GET` but only for the head
3. `POST`: post data to the uri; data is in the body; might replace existing data
4. `PUT`: 
5. `DELETE`: request a deletion of the page
6. `CONNECT`: HTTP/1.1
7. `OPTIONS`: allow the user to request for info about the server
8. `TRACE`: mostly used for diagnostic purpose



`GET` will attach data on the URL, while `POST` will attach data in the package. Thus `POST` is safer.
