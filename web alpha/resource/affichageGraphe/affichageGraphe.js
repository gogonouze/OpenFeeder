<script src="Chart.js"></script> //path ou se trouve chart.js

<canvas id="monGraphe" width="400" height="400"></canvas> // définition de l'espace du graphe

<script>
var ctx =document.getElementById('monGraphe');
var monGraphe = new Chart(ctx, {
  type: bar, //type digramme en barres
  data: {
    labels: ['Rouge','Bleu','Jaune','Vert','Mauve','Orange'],
    datasets: [{
      label: '# of visits',
      data: [12,19,20,5,4,14],
      backgroundColor: [
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(153, 102, 255, 0.2)',
        'rgba(255, 159, 64, 0.2)'
      ],
      borderColor: [
        'rgba(255, 99, 132, 1)',
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
        ticks:{
          beginAtZero: true
        }
      }]

    }
  }
});
</script>
