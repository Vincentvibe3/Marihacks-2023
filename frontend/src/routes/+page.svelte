<script lang="ts">
  import { Button, ContentContainer, Header, NumberInput, Scaffold, Text, TextInput } from "nota-ui";
  import { onMount } from "svelte";

	export let sleepStart:number
	export let sleepEnd:number

	let sleepChart:HTMLCanvasElement

</script>
<Scaffold>
	<Header slot="header">
		Title
	</Header>
	<form method="post">
		<ContentContainer>
			<Text tag="label" caption>
				When did you start sleeping
			</Text>
			<NumberInput name="start" bind:text={sleepStart}></NumberInput>
			<Text tag="label" caption>
				When did you wake up?
			</Text>
			<NumberInput name="end" bind:text={sleepEnd}></NumberInput>
			<Button>
				Submit
			</Button>
		</ContentContainer>
	</form>
</Scaffold>
