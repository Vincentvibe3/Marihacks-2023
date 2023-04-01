<script lang="ts">
    import {Button, ModalController, Navbar, SiteLayout} from "nota-ui"
  import { onMount } from "svelte";
    import { transparent, userToken } from "../stores" 

    let loggedIn:boolean

    onMount(()=>{
        loggedIn=document.cookie.includes("loggedIn=true")
    })

</script>
<svelte:head>
    <link rel="stylesheet" href="/src/global.css">
</svelte:head>
<ModalController></ModalController>
<SiteLayout>
    <Navbar alwaysOpaque={$transparent} slot="navbar" reverse>
        <svelte:fragment slot="title">
            BetterSleep
        </svelte:fragment>
        {#if loggedIn}
            <form action="http://127.0.0.1:5000/logout">
                <Button type="submit">Logout</Button>
            </form>
        {/if}
    </Navbar>
    <slot></slot>
</SiteLayout>