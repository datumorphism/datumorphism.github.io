---
layout: til
title: "VSCode Setup Tests when Module is in a Different Folder"
date: 2021-08-31
author: Lei Ma
categories:
    - misc
tags:
    - 'VSCode'
summary: Use .env file
references:
  - name: "Using Python environments in VS Code"
    link: "https://code.visualstudio.com/docs/python/environments#_use-of-the-pythonpath-variable"
---

1. Create a `.env` file.
2. Add `PYTHONPATH=src` to the `.env` file.
3. Let vscode know about the `.env` file by adding `"python.envFile": "${workspaceFolder}/.env"` to `.vscode/settings.json`.
4. Reload window to allow the test discovery to use the new configs.