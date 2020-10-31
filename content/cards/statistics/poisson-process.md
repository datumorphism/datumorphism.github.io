---
title: "Poisson Process"
date: 2019-06-18
category:
- 'Statistics'
tags:
- 'Statistics'
- 'Poisson Process'
references:
- name: axelpale/poisson-process
  link: https://github.com/axelpale/poisson-process
---

## Poisson Process

{{< rawhtml >}}
<div id="graph"></div>
{{< /rawhtml >}}

## Statistics

{{< rawhtml >}}
<div id="graph_rate"></div>

<div id="graph_interval_hist"></div>

<script src="/assets/utilities/js/poisson-process.min.js"></script>

<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>

<script>
        // define getUnixTime
    Date.prototype.getUnixTime = function () {
        return this.getTime() / 1000 | 0
    };
    if (!Date.now) Date.now = function () {
        return new Date();
    }
    Date.time = function () {
        return Date.now().getUnixTime();
    }

    POISSON_EVENT_RATE = 1

    function get_event_time() {
        var time = new Date();
        return time
    }

    all_event = []
    all_event_diff = []

    var data = [{
        x: [get_event_time],
        y: [1],
        mode: 'markers',
        line: {
            color: '#80CAF6'
        }
    }]

    var layout = {
        title: {
            text: 'Poisson Process'
        },
        xaxis: {
            title: {
                text: 'Event Time'
            },
        }
    };

    var layout_rate = {
        title: {
            text: 'Average Rate of the Poisson Process'
        },
        xaxis: {
            title: {
                text: 'Event Time'
            },
        },
        yaxis: {
            title: {
                text: 'Average Event Rate per Second'
            },
            rangemode: 'tozero'
        }
    };

    var data_rate = [{
        x: [get_event_time],
        y: [POISSON_EVENT_RATE],
        mode: 'lines+markers',
        line: {
            color: '#80CAF6'
        }
    }]

    Plotly.plot('graph', data, layout);

    Plotly.plot('graph_rate', data_rate, layout_rate)

    var p = poissonProcess.create(POISSON_EVENT_RATE * 1000, function emit_event() {

        var time = get_event_time();
        console.log('event at: ', time)
        time_unix_time = time.getUnixTime()

    time_diff = time_unix_time - all_event[all_event.length-1]
    all_event_diff.push(time_diff)
    all_event.push(time_unix_time)

        var update = {
            x: [
                [time]
            ],
            y: [
                [1]
            ]
        }

        var olderTime = time.setMinutes(time.getMinutes() - 1);
        var futureTime = time.setMinutes(time.getMinutes() + 1);

        var minuteView = {
            xaxis: {
                type: 'date',
                range: [olderTime, futureTime],
                title: {
                    text: 'Event Time'
                }
            }
        };

        Plotly.relayout('graph', minuteView);
        Plotly.extendTraces('graph', update, [0])

        // calculate average
        all_event_rate = all_event.length / (all_event[all_event.length - 1] - all_event[0])

        var update_rate = {
            x: [
                [time]
            ],
            y: [
                [all_event_rate]
            ]
        }

        var olderTime = time.setMinutes(time.getMinutes() - 1);
        var futureTime = time.setMinutes(time.getMinutes() + 1);

        var minuteView = {
            xaxis: {
                type: 'date',
                range: [olderTime, futureTime],
                title: {
                    text: 'Event Time'
                }
            }
        };

        Plotly.relayout('graph_rate', minuteView);
        Plotly.extendTraces('graph_rate', update_rate, [0])

        // interval distribution

        data_interval_hist = [{
            x: all_event_diff,
            type: 'histogram',
        }]

        layout_interval_hist = {
            xaxis: {
                title: {
                    text: 'Event Interval'
                }
            }
        };

        Plotly.newPlot('graph_interval_hist', data_interval_hist, layout_interval_hist)
    })

    p.start()
        </script>
{{< rawhtml >}}