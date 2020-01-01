---
title: "Terminal"
excerpt: "work more efficiently"
date: 2019-12-31
toc: true
category:
- 'Tools'
tag:
- 'Tools'
- 'Command Line'
- 'Terminal'
weight: 0
references:
- name: 'Must Have Git Aliases: Advanced Examples'
  link: http://durdn.com/blog/2012/11/22/must-have-git-aliases-advanced-examples/
---




## Navigating

Some tips to help data scientist navigate faster in terminal.


### `pushd`, `popd` and `dirs`

1. `pushd` to register **and** change directories: `pushd folder_name` will change current directory to `folder_name` and register the folder `folder_name` in our **stack**. If no folder name is passed onto the command, it will be default to `$HOME` folder.
2. `popd` to go to the last directory in the **stack** and remove it from the **stack**. In this example, `popd` will change the current working directory to `folder_name`.
3. `dirs` will list all working directories registered in the **stack**. The current working directory will always be in the stack.

### Moving in Commands

1. `ctrl+a`: to the beginning of line
2. `ctrl+e`: to the end of the line


## MISC

### Long Commands

1. `ctrl+x e`: start using the default editor to edit the command. For example, I started to type in a command and it is getting too long, I would prefer a better editor.
