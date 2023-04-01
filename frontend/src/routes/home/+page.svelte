<script lang="ts">
    import { Button, CardLink, ContentContainer, Header, Link, Scaffold } from 'nota-ui';
import type { PageData } from './$types';
    
    export let data: PageData;
</script>
<Scaffold>
    <Header img="dog.jpg" slot="header">
        BetterSleep
    </Header>
    <ContentContainer>
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
    </ContentContainer>
    <ContentContainer>
        
    </ContentContainer>
    <ContentContainer alignment="space-between">
        <ContentContainer>
            <Button on:click={()=>{document.location.href = "/login"}}>
                Login
            </Button>
            <Button on:click={()=>{document.location.href = "/register"}}>
                Register
            </Button>
        </ContentContainer>
        <Link href="https://www.cdc.gov/sleep/about_sleep/sleep_hygiene.html">How do I sleep better?</Link>
    </ContentContainer>
</Scaffold>