---
title: "Bloom Filter"
date: 2023-10-30
categories:
  - "Dev"
tags:
  - "Dev"
references:
  - name: "ByteByteGo. Bloom Filters. In: Real-world Examples - YouTube [Internet]. 6 Sep 2022 [cited 31 Oct 2023]. Available: https://www.youtube.com/watch?v=V3pzxngeLqw"
    link: "https://www.youtube.com/watch?v=V3pzxngeLqw"
    key: "bytebytego_bloomfilter"
---

Bloom filter returns[^bytebytego_bloomfilter]

- probably yes, or
- no.

| | element in set | element not in set |
|----|----|----|
| bloom filter returns no | ✗ | ✓ |
| bloom filter returns probably yes | ✓ | ✓ |

## How a Bloom Filter Works

{{< youtube id="V3pzxngeLqw?start=190" >}}


[^bytebytego_bloomfilter]: {{< cite key="bytebytego_bloomfilter" >}}