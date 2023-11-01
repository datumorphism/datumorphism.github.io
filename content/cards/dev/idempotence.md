---
title: "Idempotence"
date: 2023-10-30
categories:
  - "Dev"
tags:
  - "Dev"
  - "Data"
  - "Data Pipeline"
references:
  - name: "How to make data pipelines idempotent. 13 May 2021 [cited 1 Nov 2023]. Available: https://www.startdataengineering.com/post/why-how-idempotent-data-pipeline/"
    link: "https://www.startdataengineering.com/post/why-how-idempotent-data-pipeline/"
---

Data pipelines fails. Just like rebooting a system, a first fix if we don't spot any obvious error message is to retry.

A secret weapon to make sure retry works is to make our data pipeline idempotent.
