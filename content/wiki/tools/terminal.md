---
title: "Terminal"
description: "work more efficiently"
date: 2019-12-31
category:
- 'Tools'
tags:
- 'Tools'
- 'Command Line'
- 'Terminal'
references:
- name: 'Rapidly invoke an editor to write a long, complex, or tricky command'
  link: https://app.enkipro.com/#/public/insight/557a202244b51154005882a2?signedUp=1
weight: 4
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
