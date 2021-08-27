---
title: "Git"
description: "git the tool you need for your everyday work"
date: 2016-06-22
categories:
- 'Tools'
tags:
- 'Tools'
- 'Command Line'
- 'Git'
weight: 5
references:
- name: 'Must Have Git Aliases: Advanced Examples'
  link: http://durdn.com/blog/2012/11/22/must-have-git-aliases-advanced-examples/
- name: 'Setting up a repository @ atlassian.com'
  link: https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-config
---

## Git Services


- GitHub
- Bitbucket
- GitLab


## Using Git with GUI

There are huge amounts of git commands! There are also a lot of GUIs if you don't like command line.

- [GitHub Desktop](https://desktop.github.com/)
- [GitKraken](https://www.gitkraken.com/)
- [SourceTree](https://www.sourcetreeapp.com/)
- ...


## Useful Commands

-  To check all the commits related to a file, use ``git log -u``.
-  Try out ``git log -g`` before determining which reflog to deal with.
-  To compare the changes with the last commit, use
   ``git diff --cached HEAD~1``.





## Useful Alias

A very useful article here: [Must Have Git Aliases: Advanced Examples](http://durdn.com/blog/2012/11/22/must-have-git-aliases-advanced-examples/).


-  ``git config --global alias.unstage 'reset HEAD --'``
-  ``git config --global alias.last 'log -1 HEAD'``

Among ``[alias]`` section of ``~/.gitconfig`` file:

-  ``ll = log --pretty=format:"%C(yellow)%h%Cred%d\\ %Creset%s%Cblue\\ [%cn]" --decorate --numstat``



## FAQ


P: **I am too lazy to type in ``git add .``.**

S: The magic potion is ``git commit -a`` which will do the staging and
commit at the same time.

P: **What has been changed since the latest stage?**

S: ``git diff`` shows that.

P: **I typed in the wrong commit message.**

S: ``git commit --amend`` will allow you to change the commit message
you typed in before.

P: **I forgot to put add some files.**

S: Just add the file and use ``git commit --amend``. This will allow you
to replace the previous commit.

P: **I accidentally added a file to staging.**

S: Should unstage the file. ``git reset HEAD filename.md`` will do.

P: **I want to discard the changes I made since the latest commit.**

S: **This can be dangerous.** ``git checkout -- filename.md`` can revert
everything back to the last commit. But it discards all the changes and
can not be recovered. DO NOT USE IT.

P: **I need to check what has changed in every commits.**

S: ``git log --stat`` will show the changed files.

P: **I want to create a new branch based on the current branch.**

S: ``git checkout -b newbranchname`` is for you.

P: **I hate a branch called “wth” and want to delete it.**

S: ``git branch -d wth``.

P: **I want to change the name of a branch “wth” to “wtf”.**

S: ``git branch -m wth wtf`` or checkout to the branch “wth” and use
``git branch -m wtf``.

P: **Merge “goaway” branch to master branch.**

S: Checkout to master branch and ``git merge goaway``.

P: **Merge conflicts?**

S: Check the conflicts using ``git status``. Open up the conflict file
and you will see.

P: **So hard to resolve the conflicts.**

S: ``git mergetool`` will use a graphical tool.


## Git Server

It is not necessary to use hosted git services like github.com. Git remote can be on your local laptop or simply on another laptop that can be accessed by your local repo.

### A Very Basic Git Server

Since git is de-centralized, it would be nice to in fact create multiple 'backups' on different machines. A git server would do this perfectly. The bottom lines is you set up a git server and work everywhere even on a new computer.

How then?

1. [set up a git server](https://git-scm.com/book/en/v2/Git-on-the-Server-Setting-Up-the-Server)
2. Initialize a git repo **on server** so that you can push to.

   ```bash
   cd <the path you want to put your git folder>
   git init --bare yourreponame.git
   ```

   Then a folder named `yourreponame.git` will be created under `<the path you want to put your git folder>`.
3. One your local machine, using `git clone ssh://<yourusername>@<your.server.name>/<path to repo>` will clone the empty repo to your local machine.


Here I'll use my own machine as an example. After setting up the git server, I create initialized empty git repo on this server, under path `/home/neutrino/gitserver/` (where neutrino is my user name on this ubuntu machine)

```bash
git init --bare codebase.git
```

Then I find this folder named `codebase.git` under this path `/home/neutrino/gitserver/`. The work on the server-side is done now. This server has a name `physicists.edu` (which I made up), on my local machine I clone it by

```bash
git clone ssh://neutrino@physicists.edu/home/neutrino/gitserver/codebase.git
```

Whatever follows is to cd to this folder and start working on local machine then add, commit, and push.

### Push Existing Repos


What if I already have a repo locally and need to push it to this new server? Use `git remote add `. Here is an example.

```bash
git remote add newgitserver ssh://neutrino@physicists.edu/home/neutrino/gitserver/codebase.git
```

Change `newgitserver` to whatever you like. After that `git push newgitserver` will push the codes to the new server.

Alternatively, you can change `.git/config` and name this new one the origin.



## Using GitLab


Check out the [instructions](https://about.gitlab.com/).