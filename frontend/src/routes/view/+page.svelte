<script lang="ts">
  	import { onMount } from 'svelte';
    import type { PageData } from './$types';
    import { ContentContainer, Scaffold } from 'nota-ui';

	let sleepChart:HTMLCanvasElement
	let sleepTime:HTMLCanvasElement

	let hours= []
	let day = []
	let awake = []
	let asleep =[]

    onMount(async ()=>{
		await getData()
		console.log(hours)
		console.log(day)
		console.log(awake)
		console.log(asleep)
		new Chart(
			sleepTime,
			{
				type:'line',
				data:{
					labels:day,//['Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday', 'Satruday', 'Sunday'],
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
					labels: day,//['Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday', 'Satruday', 'Sunday'],
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
// {
// 	data:[
// 		{
// 			hours:6,
// 			day:"monday",
// 			awake:8,
// 			asleep:22
// 		},
// 		{
// 			hours:6,
// 			day:"monday",
// 			awake:8,
// 			asleep:22
// 		}
// 	]
// }


	async function getData() {
		const response = await fetch("http://127.0.0.1:5000/getUserSleepData", {credentials: 'include'})
		let data = await response.json()
		for (let Day of data.data){
			hours.push(Day.hours),
			day.push(Day.day),
			awake.push(Day.asleep),
			asleep.push(Day.awake)
		}
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