---
title: "Machine Learning in Production"
description: ""
date: "2023-10-25"
categories:
  - "MLOps"
tags:
  - "MLOps"
  - "Production"
references:
  - name: "ml-ops.org. [cited 1 Nov 2023]. Available: https://ml-ops.org/content/state-of-mlops"
    link: "https://ml-ops.org/content/state-of-mlops"
  - name: "ml-ops.org. [cited 1 Nov 2023]. Available: https://ml-ops.org/content/phase-zero"
    link: "https://ml-ops.org/content/phase-zero"
weight: 21
published: false
---

```mermaid
---
title: Machine Learning System
---
flowchart TD

subgraph data["1. Data"]
data_source_a["Data Source A"]
data_source_b["Data Source A"]
data_source_yet_another["..."]

subgraph raw_data["Raw Data"]

raw_data_storage["Raw Data Storage"]
raw_data_reading["Reading Raw Data"]
raw_data_q_size{{"Q: Data Size"}}
raw_data_q_freshness{{"Q: Data Freshness"}}
end

data_source_a --> raw_data
data_source_b --> raw_data
data_source_yet_another --> raw_data

data_validation["Data Validation"]

raw_data --> data_validation

data_monitoring["Data Monitoring"]
raw_data --> data_monitoring
end

subgraph experimentation["1.5. Experimentation"]

end

subgraph training["2. Training"]

end

subgraph serving["3. Serving"]

end

subgraph evaluation["4. Evaluation"]

end

subgraph production["5. Production"]

end


data -.-> training
data -.-> experimentation
experimentation -.- training
experimentation -.-> evaluation

training -.-> evaluation
evaluation -.- serving

training -.-> serving
serving -.-> production
```


## Evaluation

Evaluation is crucial to a production machine learning system.

- Online
  - Guardrails and real time monitoring
  - KPIs
  - Overarching metrics
- Offline
  - KPIs
  - Performance of each component of the system
  - Bucketing
  - Simulating use cases


## Production

- Monitoring
  - System bias
    - Pricing system recommending higher prices for an auction process.

