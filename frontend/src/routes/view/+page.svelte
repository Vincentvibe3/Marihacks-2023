<script lang="ts">
  import { onMount } from 'svelte';
    import type { PageData } from './$types';
    
    export let data: PageData;

    let sleepChart:HTMLCanvasElement

    onMount(()=>{
		new Chart(
			sleepChart, {
				type:'bar',
				data: {
					labels: ['Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday', 'Satruday', 'Sunday'],
					datasets: [{
						label: 'Hours of sleep',
						data: [12, 19, 3, 5, 2, 3],
						borderWidth: 1
					}]
					},
					options: {
					scales: {
						y: {
						beginAtZero: true
						}
					}
				}
			}
		)
	})
</script>
<canvas bind:this={sleepChart} id="sleepChart"></canvas>
<svelte:head>
	<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</svelte:head>