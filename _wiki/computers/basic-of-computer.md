---
title: "Basic of Computers"
excerpt: "Essential knowledge of computers"
last_modified_at: 2018-09-13
toc: true
category:
- 'Computer'
tag:
- 'Computer'
- 'Basics'
references:
- name: "How integers are stored in memory using two’s complement"
  title: 'https://medium.com/@LeeJulija/how-integers-are-stored-in-memory-using-twos-complement-5ba04d61a56c'
notify: 'I am transitioning from a physicist to a data scientist. While I am exploring the world of data, I find that I need to know some basics about computers.'
weight: 2
---

## Storage, Precision, Error, etc

To have some understanding of how the numbers processed in computers, we have to understan how the numbers are stored first.

Computers stores everything in binary form [^1]. Suppose we randomly get some segments in the memory, we have no idea what that stands for since we do not know the type of data it represents.

Some of the most used data types in data science are

1. integer,
2. float,
3. string,
4. time.


### Integers

Integers can occupy $2^0$, $2^1$, $2^2$, $2^3$ bytes in memory. 

```
1 byte : | | | | | | | | |
2 bytes: | | | | | | | | | | | | | | | | |
4 bytes: | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
...
```
Each of the blocks is 1 bit.

Integers can be

1. Unsigned
2. Signed

The sign can occupy one bit. However, the compiler has to know that this is a signed number otherwise it iterprets it into different numbers.
```
|1|0|0|1|0|1|0|1|
```

### Float

In computers, floating-point representation of a number is

\begin{equation}
   S\times M \times b^{E-e},
\end{equation}


where $S$ is the sign, $M$ is the mantissa, $E$ is the integer exponent, $b$ is the base and $e$ is the bias of the exponent.

**Round off** is the bias from the machine accuracy and it accumulates.

**Truncation error** is the difference between  the true answer and teh answer obtained. The reason for this is that we are doing numerical calculations by descretizing the functions. This error is the discrepancy on a ideal computer that n round off is present.

As the round off error gets magnified and finally swamp the useful answer in the calculation, the method is unstable. An algrimth like this can work on a ideal computer but not a practical one.


[^1]: I have always been speculating that we probably would have a lot of decimal computer theories if Charles Babbage built that difference engine.