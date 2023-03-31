<script lang="ts">
    import {Navbar, SiteLayout} from "nota-ui"
</script>
<svelte:head>
    <link rel="stylesheet" href="/src/global.css">
</svelte:head>
<SiteLayout>
    <Navbar slot="navbar">
        <svelte:fragment slot="title">
            Title
        </svelte:fragment>
    </Navbar>
    <slot></slot>
</SiteLayout>