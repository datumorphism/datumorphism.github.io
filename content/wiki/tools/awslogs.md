---
title: "Amazon CloudWatch Logs"
description: "CloudWatch logs as a tool for pipeline logs"
date: 2019-03-11
category:
  - 'Tools'
tags:
  - 'Tools'
  - AWS
references:
  - name: "Built-in magic commands for Jupyter"
    link: https://ipython.readthedocs.io/en/stable/interactive/magics.html
  - name: AWS Cloudwatch
    link: https://aws.amazon.com/cloudwatch/
weight: 2
---

## Why

Suppose we have all kinds of pipelines written in different languages, using different tools, and located in different places. It would be frustrating to pull out the logs.

This is why we need a centralized log service, for example [cloudwatch](https://aws.amazon.com/cloudwatch/).

## Sending logs to CloudWatch

First of all, send your logs to awslogs. The easies way is to use [boto](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html).

## Retrieving and Analyzing Logs

{{< message class="info" >}}
First of all, we need this: [awslogs](https://github.com/jorgebastida/awslogs).
{{< /message >}}

With the logs sent to cloudwatch, we then could read out the logs using the following command:

```
awslogs get etl-tools --start='1d ago' --timestamp --output text | grep error
```

This will print out the logs 1 day ago. Read the [awslogs documentation](https://github.com/jorgebastida/awslogs) for more information.

## FAQ

### How to print out the neighouring lines

{{< message class="info" >}}
More about grep: [GNU Grep 3.3](https://www.gnu.org/software/grep/manual/grep.html).
{{< /message >}}

The following command will print out 10 lines before and 10 lines after this line with error.

```
awslogs get etl-tools --start='1d ago' --timestamp --output text | grep -10 error
```

The following command will only print out the 10 lines after this error line.

```
awslogs get etl-tools --start='1d ago' --timestamp --output text | grep -A 10 error
```

Similarly, the following command will print out the 10 lines before this error line.

```
awslogs get etl-tools --start='1d ago' --timestamp --output text | grep -B 10 error
```


### Oh, too many logs

Dump the relavent logs into a file

```
awslogs get etl-tools --start='1d ago' --timestamp --output text | grep error &> error.log
```

Then read out the file using whatever text editor you like to locate the problem.



