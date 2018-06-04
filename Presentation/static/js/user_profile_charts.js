

function draw_gauge_chart(){

    // ELO GAUGE CHART
var chart = new Chartist.Pie('#elo_chart',
    {
        series: [160, 60 ],
        labels: ['', '']
    }, {
        donut: true,
        donutWidth: 20,
        startAngle: 210,
        total: 260,
        showLabel: false,
        plugins: [
            Chartist.plugins.fillDonut({
                items: [{
                    content: '<i class="fa fa-tachometer"></i>',
                    position: 'bottom',
                    offsetY : 10,
                    offsetX: -2
                }, {
                    content: '<h3>160.25<span class="small"></span></h3>'
                }]
            })
        ],
    });

chart.on('draw', function(data) {
    if(data.type === 'slice' && data.index == 0) {
        // Get the total path length in order to use for dash array animation
        var pathLength = data.element._node.getTotalLength();

        // Set a dasharray that matches the path length as prerequisite to animate dashoffset
        data.element.attr({
            'stroke-dasharray': pathLength + 'px ' + pathLength + 'px'
        });

        // Create animation definition while also assigning an ID to the animation for later sync usage
        var animationDefinition = {
            'stroke-dashoffset': {
                id: 'anim' + data.index,
                dur: 1200,
                from: -pathLength + 'px',
                to:  '0px',
                easing: Chartist.Svg.Easing.easeOutQuint,
                fill: 'freeze'
            }
        };

        // We need to set an initial value before the animation starts as we are not in guided mode which would do that for us
        data.element.attr({
            'stroke-dashoffset': -pathLength + 'px'
        });

        // We can't use guided mode as the animations need to rely on setting begin manually
        // See http://gionkunz.github.io/chartist-js/api-documentation.html#chartistsvg-function-animate
        data.element.animate(animationDefinition, true);
    }
});



}

// ELO TRESHOLD CHART

function draw_treshold_chart(){

        new Chartist.Line('#elo_evolution', {
          labels: ['Jan', 'Feb', 'Mar', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
          series: [
            [5, -4, 3, 7, 20, 10, 3, 4, 8, -10, 6, -8]
          ]
        }, {
          showArea: true,
          axisY: {
            onlyInteger: true
          },
          plugins: [
            Chartist.plugins.ctThreshold({
              threshold: 4
            })
          ],
            height: 300
        });

}



function draw_bar_chart(lessons,exercises,homeworks){

    // Resolved by far bar chart
    new Chartist.Bar('#resolved_by_far', {
      labels: ['Lessons', 'Exercises', 'Homeworks'],
      series: [lessons,exercises,homeworks]
    }, {
      distributeSeries: true
    });

}



function get_data_for_bar_chart(callback){

    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)


            var json = JSON.parse(xmlHttp.responseText);

            var lessons = json['lessons'];
            var exercises = json['exercises'];
            var homeworks = json['homeworks'];

            console.log(lessons,exercises,homeworks);
            callback(lessons,exercises,homeworks);
    };
    xmlHttp.open("GET","http://127.0.0.1:5000/progress/resolved/18" , true); // true for asynchronous
    xmlHttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlHttp.send(null);

}

function get_data_for_treshold_chart(callback){

    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)


            var json = JSON.parse(xmlHttp.responseText);
            console.log(lessons,exercises,homeworks);
            callback(lessons,exercises,homeworks);
    };
    xmlHttp.open("GET","http://127.0.0.1:5000/progress/resolved/18" , true); // true for asynchronous
    xmlHttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlHttp.send(null);
}

get_data_for_bar_chart(draw_bar_chart);
