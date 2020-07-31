    // Line
var ctx = document.getElementById("myChart").getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["轻型卡车", "SUV/MPV", "集装箱卡车", "皮卡车", "工程车辆", "轿车"],
        datasets: [{
            label: '按车型分布统计',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});

//pie
var ctxP = document.getElementById("pieChart").getContext('2d');
var myPieChart = new Chart(ctxP, {
    type: 'pie',
    data: {
        labels: ["超标", "合格", "无车牌", "无效"],
        datasets: [{
            data: [8, 72, 9, 11],
            backgroundColor: ["#F7464A", "#00C851", "#FDB45C", "#f5f5f5"],
            hoverBackgroundColor: ["#FF5A5E", "#5AD3D1", "#FFC870", "#A8B3C5"]
        }]
    },
    options: {
        responsive: true,
    }
});


//line
var ctxL = document.getElementById("lineChart").getContext('2d');
var myLineChart = new Chart(ctxL, {
    type: 'line',
    data: {
        labels: ["1日", "5日", "10日", "15日", "20日", "25日", "30日"],
        datasets: [{
            label: "汽油车辆",
            backgroundColor: [
                'rgba(105, 0, 132, .2)',
            ],
            borderColor: [
                'rgba(200, 99, 132, .7)',
            ],
            borderWidth: 2,
            data: [65, 59, 80, 81, 56, 55, 40]
        },
            {
                label: "柴油车辆",
                backgroundColor: [
                    'rgba(0, 137, 132, .2)',
                ],
                borderColor: [
                    'rgba(0, 10, 130, .7)',
                ],
                data: [28, 48, 40, 19, 86, 27, 90]
            }
        ]
    },
    options: {
        responsive: true
    }
});


//radar
var ctxR = document.getElementById("radarChart").getContext('2d');
var myRadarChart = new Chart(ctxR, {
    type: 'radar',
    data: {
        labels: ["CO", "CO2", "HC", "NO", "黑度", "不透光度"],
        datasets: [{
            label: "汽油车辆",
            data: [165, 159, 190, 181, 156, 155],
            backgroundColor: [
                'rgba(105, 0, 132, .2)',
            ],
            borderColor: [
                'rgba(200, 99, 132, .7)',
            ],
            borderWidth: 2
        }, {
            label: "柴油车辆",
            data: [128, 148, 140, 119, 196, 127],
            backgroundColor: [
                'rgba(0, 250, 220, .2)',
            ],
            borderColor: [
                'rgba(0, 213, 132, .7)',
            ],
            borderWidth: 2
        }]
    },
    options: {
        responsive: true
    }
});
