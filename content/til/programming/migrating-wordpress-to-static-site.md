---
layout: til
title: "Migrating Wordpress to Static"
date: 2015-12-04
author: Lei Ma
category:
- programming
- basics
tags:
- Web
excerpt: Migrating Wordpress to Static
---



The following command can mirror a whole website including a wordpress into a static html site locally.

```
# Mirror website to a static copy for local browsing.
# This means all links will be changed to point to the local files.
# Note --html-extension will convert any CGI, ASP or PHP generated files to HTML (or anything else not .html).

wget --mirror -w 2 -p --html-extension --convert-links -P <dir> http://www.yourdomain.com
```

But this will get a static site with absolute links. To get a site that works as relative links for wordpress, use this plugin in first:

* [staticpress](https://github.com/megumiteam/staticpress)
