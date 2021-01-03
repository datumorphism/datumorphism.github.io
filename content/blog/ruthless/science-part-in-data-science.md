---
layout: post
title: "The Science Part in Data Science"
category:
- blog
tags:
- Ruthless Data Scientist
comments: true
author: "LM"
mermaid: true
published: true
---



{{< mermaid >}}
graph TD;
    s1(An Idea)-->d1{Is this idea in the current literature?};
	d1{Is this idea in the current literature?}-->|Yes|b1(Fail);
	d1{Is this idea in the current literature?}-->|No|b2[Weeks of work];
	b2[Weeks of work]-->b1(Fail);
{{< /mermaid >}}
