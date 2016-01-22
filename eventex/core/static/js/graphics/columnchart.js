$(function () {
    var url = "/inscricao/json/column/";

    $.getJSON(url, function(res){
        console.log(res);
        /* Transformando o dicionário em lista.
           Com o comando map eu coloco uma lista dentro da outra,
           necessário para este tipo de gráfico. */
        var paid_data = res.map(function (v) {
            return [v.label, v.value]
        });

        console.log(paid_data);

        $('#columnchart').highcharts({
            chart: {
                type: 'column'
            },
            title: {
                text: 'Quantidade de pessoas que já pagaram'
            },
            xAxis: {
                type: 'category'
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Quantidade'
                }
            },
            legend: {
                enabled: false
            },
            colors: ['#44AD41', '#DE2121'],
            series: [{
                name: 'Sim',
                data: paid_data,
                colorByPoint: true,
                dataLabels: {
                    enabled: true,
                    align: 'center',
                    color: '#FFFFFF',
                    y: 25, // 25 pixels down from the top
                    style: {
                        fontSize: '15px'
                    }
                }
            }],
        });
    });
});