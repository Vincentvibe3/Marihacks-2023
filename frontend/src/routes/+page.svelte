<script lang="ts">
  import { Button, ContentContainer, Header, NumberInput, Scaffold, Text, TextInput } from "nota-ui";
  import { onMount } from "svelte";

	export let sleepStart:number
	export let sleepEnd:number

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
<svelte:head>
	<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</svelte:head>
<Scaffold>
	<Header slot="header">
		Title
	</Header>
	<ContentContainer>
		<Text tag="label" caption>
			When did you start sleeping
		</Text>
		<NumberInput bind:text={sleepStart}></NumberInput>
		<Text tag="label" caption>
			When did you wake up?
		</Text>
		<NumberInput bind:text={sleepEnd}></NumberInput>
		<Button>
			Submit
		</Button>
	</ContentContainer>
	<canvas bind:this={sleepChart} id="sleepChart"></canvas>
</Scaffold>
