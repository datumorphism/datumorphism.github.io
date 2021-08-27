---
title: "Dashboards"
date: 2021-08-27
categories:
  - "Data Visualization"
tags:
  - "Data Visualization"
  - "Dashboard"
references:
  - name: "Hullman J, Gelman A. Designing for interactive exploratory data analysis requires theories of graphical inference. Harvard Data Science Review. 2021. doi:10.1162/99608f92.3ab8a587"
    link: "https://hdsr.mitpress.mit.edu/pub/w075glo6/release/2"
    key: "Hullman2021"
  - name: "streamlit"
    link: "https://streamlit.io/"
  - name: "plotly dash"
    link: "https://plotly.com/dash/"
weight: 8
---

Building interactive dashboards is not easy task. However, with the right tool, we can build a prototype fast.

## Theories

Dashboard building seems to be a task to build whatever charts the business would like to add.

However, theories are required to build quality dashboards[^Hullman2021].

{{< message title="AmNeumarkt/253" >}}

I wrote a comment about this: [AmNeumarkt/253](https://t.me/amneumarkt/253).

Creating visualizations seems to be a creative task. At least for entry-level visualization tasks, we follow our hearts and build whatever is needed. However, visualizations are made for different purposes. Some visualizations are simply explorations and for us to get some feelings on the data. Some others are built for the validation of hypotheses. These are very different things.

Confirmation of an idea using charts is usually hard. In most cases, we need statistical tests to (dis)prove a hypothesis instead of just looking at the charts. Thus, visualizations become a tool to help us formulate a good question.

However, not everyone is using charts as hints only. Instead, many use charts to conclude. As a result, even experienced analysts draw spurious conclusions. These so-called insights are not going to be too solid.

The visual analysis seems to be an adversarial game between humans and the visualizations. There are many different models for this process. A crude and probably stupid model can be illustrated through an example of analysis by the histogram of a variable.
The histogram looks like a bell. It is symmetric. It is centered at 10 with an FWHM of 2.6. I guess this is a Gaussian distribution with a mean 10 and sigma 1. This is the posterior p(model | chart).

- Imagine a curve like what was just guessed on top of the original curve. Would my guess and the actual curve overlap with each other?
- If not, what do we have to adjust? Do we need to introduce another parameter?
- Guess the parameter of the new distribution model and compare it with the actual curve again.

The above process is very similar to a repetitive Bayesian inference. Though, the actual analysis may be much more complicated as the analysts would carrier a lot of prior knowledge about the generating process of the data.

Through this example, we see that integrating explorations with preliminary model building as Confirmatory Data Analysis may bring in more confidence in drawing insights from charts.

On the other hand, including complicated statistical models leads to misinterpretations since not everyone is familiar with statistical hypothesis testing. So the complexity has to be balanced.
{{< /message >}}


## Frameworks

### Streamlit

[Streamlit](https://streamlit.io/) is a fast prototyping tool.

I built a template for multi-page apps: [emptymalei/streamlit-multipage-template](https://github.com/emptymalei/streamlit-multipage-template).


### Plotly Dash

[Plotly Dash](https://plotly.com/dash/) is more versatile and faster.

Here is an example that I built: [emptymalei/schelling-model](https://github.com/emptymalei/schelling-model).


[^Hullman2021]: {{< cite key="Hullman2021" >}}