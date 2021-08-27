---
title: "Basics of Network"
description: "Essential knowledge of internet"
date: 2018-09-23
categories:
- 'Computation'
tags:
- 'Internet'
- 'Basics'
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

{{< youtube po3zYOe00O4>}}



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


## Models

### The OSI Model

Refer to [The Open Systems Interconnection Model on Wikipedia](https://en.wikipedia.org/wiki/OSI_model).


A nice visualization of the seven layers.

{{< figure src="../assets/network/complete-osi-model-2.jpeg" caption="Source: https://www.studytonight.com/computer-networks/complete-osi-model" >}}




### The Internet Procotcal Suite

{{< figure src="../assets/network/800px-IP_stack_connections.svg.png" caption="Source: https://en.wikipedia.org/wiki/Internet_protocol_suite#/media/File:IP_stack_connections.svg" >}}



#### About TCP/IP

This is the Link Layer.



## IP Address and Domain

Some key concepts:

- Address
- Subnet: a sub network that shares the same subnet address
- Subnet mask: 32-bit, mask the address to specify the subnet and host
- Interface


{{< figure src="../assets/network/cisco-ip-addresses.webp" caption="Source: https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html" >}}


What is the slash 28 (/28) in the notation `255.255.255.240 (/28)`? It means 28 bits. See the illustration bellow [^cisco].

```
204.17.5.0 -      11001100.00010001.00000101.00000000
255.255.255.240 - 11111111.11111111.11111111.11110000
                  --------------------------|sub |---
```


## IaaS, Paas, Saas

- Infrastructure as a Service
- Platform as a Service
- Software as a Service



[^cisco]: [IP Addressing and Subnetting for New Users](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html)





