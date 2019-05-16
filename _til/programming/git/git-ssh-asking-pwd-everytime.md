---
layout: til
title: "Git Asks for Password Whenever I Pull or Push"
date: 2017-05-11
author: Lei Ma
comments: true
category:
- programming
tag:
- Git
excerpt: My git asks for password every time I pull or push even with ssh configured.
---



I already set all my ssh keys and used ssh for git. The repo is stored on a linux server in my office. With everything set, I expected the ssh key to work and I don't need to type in password.

However, git asks for password each time I pull or push, which made me very curious.

What I found is that I should use the short ssh name defined in ssh config instead of the full ssh path in git.

For example, I have a ssh account `mk@urmy.sunshine.com`. For convenience I defined a short name for it.

```
Host mksunshine
  Hostname urmy.sunshine.com
  IdentityFile ~/.ssh/id_rsa_sunshine
  User mk
```

If I use the full ssh path in git, such as

```
[remote "origin"]
        url =  mk@urmy.sunshine.com:~/gitserver/mkrepo.git
        fetch = +refs/heads/*:refs/remotes/origin/*
```

the git program seems to ignore the ssh settings and will ask for password.

To fix this problem, simply change the full ssh path in git config to the short name.

```
[remote "origin"]
        url =  mksunshine:~/gitserver/mkrepo.git
        fetch = +refs/heads/*:refs/remotes/origin/*
```

~~Damn. I spent almost an hour on this problem.~~
