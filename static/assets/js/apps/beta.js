var app = new Vue({
    delimiters: ["((", "))"],
    el: '#app',
    data: {
        alpha: 2,
        beta: 5
    },
    methods: {

    },
    computed: {
        x: function () {
            return x = stdlib.linspace( 0.0, 1.0, 1000 )
        },
        beta_dist: function () {
            return this.x.map(e=>stdlib.base.dists.beta.pdf( e, this.alpha, this.beta ))
        },
        beta_median: function () {
            return stdlib.base.dists.beta.median(this.alpha, this.beta )
        },
        beta_mean: function () {
            return stdlib.base.dists.beta.mean(this.alpha, this.beta )
        },
        beta_mode: function () {
            return stdlib.base.dists.beta.mode(this.alpha, this.beta )
        },
        makeGraph: function () {
            const DF = {
                x: this.x,
                y: this.beta_dist,
                type: 'line'
            };

            const layout = {
                title: `Beta`,
                showLegend: true,
                displayModeBar: false
                }

            Plotly.newPlot(
                "beta-chart",
                [DF],
                layout
            );
        }
    },
    mounted: function () {
        const DF = {
            x: this.x,
            y: this.beta_dist,
            type: 'line'
        };

        const layout = {
            title: `Beta`,
            showLegend: true,
            displayModeBar: false
            }

        Plotly.newPlot(
            "beta-chart",
            [DF],
            layout
        );
    }
})

x = stdlib.linspace( 0.0, 1.0, 10000 )
alpha = 2
beta = 5
beta_1 = x.map(e=>stdlib.base.dists.beta.pdf( e, alpha, beta ))