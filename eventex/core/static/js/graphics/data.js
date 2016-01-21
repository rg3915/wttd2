// Lê os dados, que já estão em json
var json = function(callback){
var json = null;
$.ajax({
  url: "/inscricao/json/",
  type: 'GET',
  dataType: 'json',
  success: function (data) {
    json = data;
    callback(data);
  }
});
return json;
};

// Gera o gráfico
var grafico = function(dados) {
  Morris.Donut({
    element: 'donutchart',
    data: dados,
    colors: [
      '#44AD41', // verde
      '#DE2121', // vermelho
    ],
    formatter: function (x) { return x + "%"}
  });
};

// Chamando a função para gerar o gráfico
json(grafico);

// Caso queira imprimir os dados no console
/*json(function(json){
  console.log(json)
});*/
