---
title:  "StemGNN"
date: 2022-01-01
modified: 2022-01-01
subtitle: "from Spectral Temporal Graph Neural Network forMultivariate Time-series Forecasting"
speaker: "Lei Ma"
authors:
  - Lei Ma
categories:
  - graph neural network
tags:
  - graph neural network
  - graph
  - forecasting
  - time series
summary: ""
status: Done
references:
  - name: "Cao D, Wang Y, Duan J, Zhang C, Zhu X, Huang C, et al. Spectral Temporal Graph Neural Network for multivariate time-series forecasting. arXiv [cs.LG]. 2021. Available: http://arxiv.org/abs/2103.07719"
    link: http://arxiv.org/abs/2103.07719
---

- What problem is StemGNN solving:
	- intra-series temporal pattern: DFT
		- Each series
	- inter-series correlations
		- At each step, the interactions between nodes
		- reversible operator
	- Example problem
		- Covid cases: DE, AT, NL, ...
		- Predicting each country without considering the interactions between them
		- Or introduce the people flow between them
- GFT:
	- Completes DFT as it takes care of the inter-series correlations
	- one extra slide for this topic
- Convolutions on Graphs
	- one extra slide for this topic



## How to build the graph

- "self-attention":
	- outer product of key, query, as the adjacency matrix
		- key, query are of length # of ndoes


## Weights and Biases

- LC
- 1DConv
- GLU
- FC

## Experiments


- Traffic adjacency matrix
	- neighbouring sensors have higher correlations
- Covid
	- Neighbouring countries have higher correlation
	- Spetral analysis:
		- Some eigenvectors have clear meanings


## Week spots

- Paper and code are not consistent
	- https://github.com/microsoft/StemGNN/issues/12
- Static graph


## Architecture

{{< mermaid >}}
stateDiagram-v2
    with_spectral_matrix_representation: Spectral Matrix Representation
    with_temporal_patterns_in_freq_domain: Temporal Patterns in Frequency Domain
    with_latent_correlation: Latent Correlation Representation
    dft_repr: Discrete Fourier Transformed Representation
    conv_dft_repr: Convolved DFT Representation

    [*] --> with_latent_correlation: Latent Correlation Layer

    with_latent_correlation --> with_latent_correlation

    state with_latent_correlation {

        state with_spectral_matrix_representation {
            [*] --> dft_repr: Discrete Fourier Transform

            dft_repr --> conv_dft_repr: 1DConv

            conv_dft_repr --> gated_conv_dft_repr: Gated Linear Unit

            gated_conv_dft_repr --> inverse_dft_gated_conv_dft_repr: IDFT

        }


        [*] --> with_spectral_matrix_representation: Graph Fourier Transform
        note right of with_spectral_matrix_representation: This happens in Spe-Seq Cell

        with_spectral_matrix_representation --> with_temporal_patterns_in_freq_domain

        with_temporal_patterns_in_freq_domain --> with_conv_temporal_patterns: Graph Convolution

        with_conv_temporal_patterns --> with_timeseries_restored: IGFT

        with_timeseries_restored --> Forecast
        with_timeseries_restored --> Backcast

    }
    note right of with_latent_correlation: This is done in StemGNN Block

    with_latent_correlation --> [*]
{{< /mermaid >}}
