---
layout: til
title: "Pandas with MultiProcessing"
date: 2018-09-09
modified: 2018-09-09
author: Lei Ma
category:
- programming
- basics
tag:
- Python
- Pandas
excerpt: Adding new data to dataframe using multiprocessing
---

1. Define number of processes, `prs`;
2. Split dataframe into `prs` dataframes;
3. Process each dataframe with one process;
4. Merge processed dataframes into one.

A piece of demo code is bellow.


{% highlight python %}
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

import pandas as pd

# Create a dataframe to be processed
df = pd.read_csv('somedata.csv').reset_index(drop=True)

# Define a function to be applied to the dataframe
def nice_func(name, age):
    return (name,age)

# Apply to dataframe
def apply_to_df(df_chunks):
    df_chunks['tupled'] = df_chunks.apply( lambda x: nice_func( x['host_name'], x['host_country']), axis=1 )
    return df_chunks
    print('finished chunk')

# Divide dataframe to chunks
prs = 100 # define the number of processes
chunk_size = int(df.shape[0]/prs)
chunks = [df.iloc[df.index[i:i + chunk_size]] for i in range(0, df.shape[0], chunk_size)]

# Process dataframes
with ThreadPool(prs) as p:
    result = p.map(apply_to_df, chunks)

# Concat all chunks
df_reconstructed = pd.concat(result)
{% endhighlight %}
