---
title: "Regular Expression Basics"
description: "Some quick start material on regular expression."
date: 2018-06-20T15:58:49-04:00
category:
  - 'Basics'
tags:
  - 'Regular Expression'
  - RegEx
references:
  - name: Module Contents@Python3 Documentation
    link: https://docs.python.org/3/library/re.html#module-contents
  - name: Regex tutorial — A quick cheatsheet by examples by Jonny Fox
    link: https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285
  - name: regex101
    link: https://regex101.com/
  - name: extendsclass
    link: https://extendsclass.com/regex-tester.html
weight: 1
---

## List of Keys

### Anchors

1. at the beginning of line `^`
   ```
   import re
   p = re.compile('^T', re.I)
   line = "The email address is this this the do you see"
   result = p.findall(line)
   print(result)
   # ['T']
   ```
2. at the end of the line `$`
   ```
   import re
   p = re.compile('e$', re.I)
   line = "The email address is this this the do you see"
   result = p.findall(line)
   print(result)
   # ['e']
   ```



### Character Classes

#### Printable Characters

0. any character `.`
   ```
   import re
   p = re.compile('^T.', re.I)
   line = "The email address is this this the do you see"
   result = p.findall(line)
   print(result)
   # ['Th']
   ```
1. single character of digit `\d`
2. word **character** `\w` (including alphanumeric character and underscore):
   ```
   import re
   line = "The email address is this this the do you see"
   result = re.findall('\w', line)
   print(result)
   # ['T', 'h', 'e', 'e', 'm', 'a', 'i', 'l', 'a', 'd', 'd', 'r', 'e', 's', 's', 'i', 's', 't', 'h', 'i', 's', 't', 'h', 'i', 's', 't', 'h', 'e', 'd', 'o', 'y', 'o', 'u', 's', 'e', 'e']
   ```
3. whitespace `\s`
   ```
   import re
   line = "The email address is this this the do you see"
   result = re.findall('\sth[e|i]', line)
   print(result)
   # [' thi', ' thi', ' the']
   ```


#### Non-printable Characters

1. tabs `\t`
2. new line `\n`
3. carriage return `\r`

#### Capitalization

1. non-digit `\D`
2. non-word `\W`
3. non-blank character `\S`


### Quantifiers

1. 0 or more times `*`
   ```
   import re
   p = re.compile('^T\w*', re.I)
   line = "The email address is this this the do you see"
   result = p.findall(line)
   print(result)
   # ['The']
   ```
2. 1 or more times `+`
3. n times `{n}`
4. n1 to n2 times `{n1,n2}`
5. n or more times `{n,}`
   ```
   import re
   p = re.compile('(?:d){2,}', re.I)
   line = "The email address is this this the do you see"
   result = p.findall(line)
   print(result)
   # ['dd']
   ```


### Flags

Regex comes with several flags that can be used to define the way of searching. In the python `re` module, it is done with options of `compile` function.

1. ignoring cases `i`: `re.I` in python
   ```
   import re
   p = re.compile('the',re.I)
   line = "The email address is this this the do you see"
   result = p.findall(line)
   print(result)
   # ['The', 'the']
   ```
2. multiline `m`: `re.M` in python
3. global `g`
4. Python `re` module also provides some other flags.[^1]

### Greedy Search

1. Don't be greedy `?`: regex matches the longest strings of the pattern without `?`
   ```
   import re
   p1 = re.compile('^T.*e', re.I)
   p2 = re.compile('^T.*?e', re.I)
   line = "The email address is this this the do you see"
   result1 = p1.findall(line)
   result2 = p2.findall(line)
   print(result1)
   # ['The email address is this this the do you see']
   print(result2)
   # ['The']
   ```


### Grouping and Capturing

1. capturing `()`: matches the whole expression even with keys outside of the parenthesis but returns only the part inside `()`
   ```
   import re
   p = re.compile('th(e|i)',re.I)
   line = "The email address is this this the do you see"
   result = p.findall(line)
   print(result)
   # ['e', 'i', 'i', 'e']
   ```
2. grouping `(?:)`: `?:` disables the capturing so that the parenthesis indicates only grouping
   ```
   import re
   p = re.compile('th(?:e|i)',re.I)
   line = "The email address is this this the do you see"
   result = p.findall(line)
   print(result)
   # ['The', 'thi', 'thi', 'the']
   ```
3. either character `[]`: `[aeiou]`, `[a-z]`
   ```
   import re
   p = re.compile('th[ei]',re.I)
   line = "The email address is this this the do you see"
   result = p.findall(line)
   print(result)
   # ['The', 'thi', 'thi', 'the']
   ```
4. group name `T(?<groupname>he)`
5. referencing nth group `\n`
6. referencing group by name `\k<groupname>`


### Special Characters

1. escape `\`: is used to escape some special characters

### Boundaries

1. boundaries of words `\b` (depends on the locale)



## Python

0. `compile`
1. `search`
2. `findall`
3. `match`
4. ...


## Useful expressions


1. `^X-.*:`: `X-`` is at the beginning of the line, followed by 0 or more characters and `:`
2. `^X-\S+:`: `X-` is at the beginning of the line, followed by 1 or more non-blank characters and `:`
3. `^X-\S+?:`: `?` means "don't be greedy"
4. `\S+@\S+`: finds email addresses
5. `^Email (\S+@\S+)`: finds the pattern but returns only the part in `()` which should be the email address
6. `[^ ]`: not space; `^` means not
7. `[a-zA-Z0-9]` means all the letters and numbers
8. `[^a-zA-Z0-9]` means neither letters nor numbers


## Links

1. [Regex tutorial — A quick cheatsheet by examples by Jonny Fox](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
2. [regex101](https://regex101.com/) is an useful website for regex.
3. Practice on repl.it
   {{< repl url="https://repl.it/@emptymalei/regular-expressions?lite=true" >}}

4. [extendsclass](https://extendsclass.com/regex-tester.html) is an online regex tester with a regular expression visualizer.


## References


[^1]: [Module Contents@Python3 Documentation](https://docs.python.org/3/library/re.html#module-contents)
