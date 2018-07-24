$(document).ready(function(){
	var ctx = document.getElementById('main_chart').getContext('2d');
	
	var config = {
		type: 'line',

		data: {
			labels: [1, 2, 3, 4, 5],
			datasets: [{
				label: 'Highest Temp',
				backgroundColor: 'rgba(255, 0, 0, 0.6)',
				borderColor: 'rgba(255, 0, 0, 0.6)',
				data: [12, 34, 12, 1, 34],
				fill: false,
			}, {
				label: 'Lowest Temp',
				fill: false,
				backgroundColor: 'rgba(0, 0, 255, 0.6)',
				borderColor: 'rgba(0, 0, 255, 0.6)',
				data: [1, 2, 4, 2, 7],
			}, {
				label: 'Median',
				fill: false,
				backgroundColor: 'rgba(0, 255, 0, 0.6)',
				borderColor: 'rgba(0, 255, 0, 0.6)',
				data: [4, 2, 1, 6, 3],
			}],
		},

		options: {
			responsive: true,
			title: {
				display: true,
				text: 'Line Chart'
			},
			tooltips: {
				mode: 'index',
				intersect: false,
			},
			hover: {
				mode: 'nearest',
				intersect: true
			},
			scales: {
				xAxes: [{
					display: true,
					scaleLabel: {
						display: true,
						labelString: 'Sample'
					}
				}],
				yAxes: [{
					display: true,
					scaleLabel: {
						display: true,
						labelString: 'Value'
					}
				}]
			}
		}

	}

	// make chart
	window.myLine = new Chart(ctx, config);
});