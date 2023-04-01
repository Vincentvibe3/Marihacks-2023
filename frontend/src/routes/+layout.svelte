<script lang="ts">
    import {ModalController, Navbar, SiteLayout} from "nota-ui"
  import { onMount } from "svelte";
    import { transparent, userToken } from "../stores" 

    let loggedIn

    onMount(()=>{
        loggedIn=document.cookie.includes("loggedIn=true")
    })

</script>
<svelte:head>
    <link rel="stylesheet" href="/src/global.css">
</svelte:head>
<ModalController></ModalController>
<SiteLayout>
    <Navbar alwaysOpaque={$transparent} slot="navbar">
        <svelte:fragment slot="title">
            Title
        </svelte:fragment>
    </Navbar>
    <slot></slot>
</SiteLayout>