---
title: "Certificate Errors in urllib"
date: 2018-06-25
authors:
  - Lei Ma
categories:
- data
tags:
- Web
- 'Web Scraping'
summary: Dealing with errors when scraping data
references:
  - name: "Worked Example: BeautifulSoup (Chapter 12)"
    link: https://www.youtube.com/watch?v=mhaHWiSPxxE
---

```python
# Import modules
import urllib.request, urllib.parse, urllib.error, ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Retrieve data
# The context = ctx will ignore the errors from certificates
url = 'https://www.google.com'
html = urllib.request.urlopen(url, context=ctx).read()
```


References: [Worked Example: BeautifulSoup (Chapter 12)](https://www.youtube.com/watch?v=mhaHWiSPxxE)
