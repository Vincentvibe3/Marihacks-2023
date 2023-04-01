<script lang="ts">
  	import { onMount } from 'svelte';
    import type { PageData } from './$types';
    import { ContentContainer, Scaffold } from 'nota-ui';
    
    export let data: PageData;

	let sleepChart:HTMLCanvasElement
	let sleepTime:HTMLCanvasElement

	let hours:unknown
	let day:unknown
	let awake:unknown
	let asleep:unknown

    onMount(()=>{
		new Chart(
			sleepTime,
			{
				type:'line',
				data:{
					labels:['Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday', 'Satruday', 'Sunday'],
					datasets:[
						{label:'Time asleep',data:/*[-20,-21,-22,-21,-22,-21,-22]*/ asleep},
						{label:'Time awake',data:/*[-6,-6,-6,-6,-6,-6,-6]*/awake}
					]
				},
				options:{
					scales:{

						y:{
							suggestedMin:-24,
							suggestedMax:0,
							ticks:{
								stepSize:2
							}
						}
					}
				}
			}
		)
		new Chart(
			sleepChart, 
			{
				type:'bar',
				data: {
					labels: ['Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday', 'Satruday', 'Sunday'],
					datasets: [{
						label: 'Hours of sleep',
						data: /*[12, 19, 3, 5, 2, 3]*/ hours,
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


	async function getData() {
		const response = await fetch("http://127.0.0.1:5000/getUserSleepData")
		let data = await response.json()
		hours = data.hours;
		day = data.day;
		awake = data.awake;
		asleep = data.asleep;



		return response.json();
	}
</script>
<Scaffold>
	<ContentContainer direction="column">
		<div class="wrapper">
			<canvas bind:this={sleepChart} id="sleepChart"></canvas>
			<canvas bind:this={sleepTime} id="sleepChart"></canvas>
		</div>
	</ContentContainer>
</Scaffold>

<svelte:head>
	<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</svelte:head>
<style>
	.wrapper {
		position: relative;
		top: 3rem;
		margin-bottom: 2rem;
		width: 100%;
	}
</style>