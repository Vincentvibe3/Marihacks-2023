<script lang="ts">
	import { Scaffold, TextInput, Text, PasswordInput, Button, Card } from 'nota-ui';
    import { onMount } from 'svelte';
    import { userToken } from '../../../stores';

    import type { ActionData } from './$types';
    
    export let form:ActionData;

    onMount(()=>{
        if (form!=null){
            $userToken= form?.token
            document.location.href = "/"
        }
    })

    let username:string
    let password:string


</script>
<img class="bg" alt="Person Sleeping" src="https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1160&q=80"/>
<Scaffold>
	<!-- <Header compact slot="header">
		Login
	</Header> -->
    <div class="loginBox" style:width="30rem">
        <Card --cardPadding="2.5rem" --cardBg="#fafafa">
            <Text tag="h1" heading3>Login</Text>
            <form action="http://127.0.0.1:5000/login" style:display="contents" method="POST">
                <Text tag="label" body2 attributes={{"for":"username"}}>Username</Text>
                <TextInput bind:text={username} name="username"></TextInput>
                <Text tag="label" body2 attributes={{"for":"password"}}>Password</Text>
                <PasswordInput name="password" bind:text={password}></PasswordInput>
                <Button type="submit">Login</Button>
            </form>
        </Card>
    </div>
</Scaffold>
<style>

    .bg {
        position: fixed;
        width: 100vw;
        height: 100vh;
        object-fit: cover;
        z-index: -1;
    }

    .loginBox{
        position: absolute;
        top: 50%;
        left:50%;
        transform: translate(-50%, -50%);
        transition: all ease-in-out 0.5s;
    }

    @media only screen and (min-width:1000px){
        .loginBox{
            left: 10%;
            transform: translate(0%, -50%);
        }
    }

</style>