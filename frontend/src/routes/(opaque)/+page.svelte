<script lang="ts">
  import { Button, ContentContainer, Header, Link, NumberInput, queueModal, Scaffold, Text, TextInput } from "nota-ui";
  import Form from "../../lib/Form.svelte";
  import { loggedIn, userToken } from "../../stores";
  import { onMount } from "svelte";
  import { page } from "$app/stores";

	export let sleepStart:number
	export let sleepEnd:number
	export let user:number
	export let day:number

	onMount(()=>{
		let loggedIn=document.cookie.includes("loggedIn=true")
		if(!loggedIn){
			document.location.href = "/home"
		}
	})

</script>
<Scaffold>
	<Header slot="header">
		Dashboard
	</Header>
	<Text tag="p" subtitle>View my sleep history</Text>
	<Link href="/view" arrow>View my sleep history</Link>
	<Link href="/leaderboard" arrow>View others</Link>
	<Text tag="p" subtitle>Add new data</Text>
	<Button on:click={()=>{queueModal(
		{
			component:Form,
			title:"Add a sleep entry"
		}
	)}}>
		Add an entry
	</Button>
</Scaffold>
