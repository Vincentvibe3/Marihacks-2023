<script lang="ts">
    import { Button, CardLink, ContentContainer, Header, Link, Scaffold } from 'nota-ui';
import type { PageData } from '../../home/$types';
    
    export let data: PageData;
</script>
<Scaffold>
    <Header position="center" img="dog.jpg" slot="header">
        Welcome to BetterSleep
    </Header>
    <ContentContainer>
        <p>
            Bettersleep is an application that allows users to track their sleep habits and compare to other users. Bettersleep trends the sleep data to allow users to see the consistency of their sleep schedule and their sleeping time, and compare that data to other users and incentivise themselves to get better quality sleep.
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