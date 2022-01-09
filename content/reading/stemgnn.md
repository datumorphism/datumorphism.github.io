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

{{< mermaid >}}
stateDiagram-v2
    with_spectral_matrix_representation: Spectural Matrix Representation
    with_temporal_patterns_in_freq_domain: Temporal Patterns in Frequency Domain

    [*] --> StemGNNBlock

    StemGNNBlock --> StemGNNBlock

    state StemGNNBlock {
        [*] --> with_spectral_matrix_representation: Graph Fourier Transform

        with_spectral_matrix_representation --> with_temporal_patterns_in_freq_domain: Spe-Seq Cell

        with_temporal_patterns_in_freq_domain --> with_conv_temporal_patterns: Graph Convolution

        with_conv_temporal_patterns --> with_timeseries_restored: IGFT

        with_timeseries_restored --> Forecast
        with_timeseries_restored --> Backcast

    }



    state with_spectral_matrix_representation {
        [*] --> dft_repr: Discrete Fourier Transform

        dft_repr --> conv_dft_repr: 1DConv

        conv_dft_repr --> gated_conv_dft_repr: Gated Linear Unit

        gated_conv_dft_repr --> inverse_dft_gated_conv_dft_repr: IDFT
    }


    StemGNNBlock --> [*]
{{< /mermaid >}}
