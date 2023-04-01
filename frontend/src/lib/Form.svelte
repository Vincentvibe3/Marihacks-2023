<script lang="ts">

  import { Button, ContentContainer, dismissModal, NumberInput,ProgressRing,Text } from "nota-ui";

  	export let sleepStart:number
	export let sleepEnd:number
	export let day:number

	let status: "loading" | "error" | "complete" | undefined

	const sendData = async () => {
		status = "loading"
		let resp = await fetch("http://127.0.0.1:5000/log", {
			method:"POST",
			credentials: 'include',
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({
				start:sleepStart,
				end:sleepEnd,
				day:day
			})
		})
		if (resp.ok){
			status="complete"
			dismissModal()
		} else {
			status="error"
		}
	}

</script>
<ContentContainer>
	<Text tag="label" caption>
		When did you start sleeping
	</Text>
	<NumberInput name="start" bind:text={sleepStart}></NumberInput>
	<Text tag="label" caption>
		When did you wake up?
	</Text>
	<NumberInput name="end" bind:text={sleepEnd}></NumberInput>
	<ContentContainer direction="column">
		<Text tag="label" caption>
			What day is the entry for?
		</Text>
		<input type="date" bind:value={day}>
		<ContentContainer>
			<Button on:click={sendData}>
				Submit
			</Button>
			{#if status!== undefined}
				<ProgressRing bind:status indeterminate></ProgressRing>
			{/if}
		</ContentContainer>
		
	</ContentContainer>
	
</ContentContainer>