const ctx = document.getElementById('myChart');
      
        new Chart(ctx, {
          type: 'bar',
          data: {
            labels: [listeStockcode], //stockcode 
            datasets: [{
              label: 'répartition des ventes par produit',
              data: [listecount], // nombre de vente de stockcode
        
              borderWidth: 2
            }]
          },
          options: {
            
            scales: {
              y: {
                beginAtZero: true
              }
            },
            plugins: {
              title: {
                  display: false,
                  text: 'Custom Chart Title',
                  padding: {
                      top: 10,
                      bottom: 30
                  }
              },
              subtitle: {
                  display: false,
                  text: 'Custom Chart Subtitle',

              }
          }
          }
        });