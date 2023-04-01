<script lang="ts">
    import { Header, Scaffold, Table, TableCell, TableHeader, TableRow, Text } from 'nota-ui';
  import { onMount } from 'svelte';

    let data = []
    let userSleep = ""

    onMount(async ()=>{
        let resp = await fetch("http://127.0.0.1:5000/leaderboard",{credentials: 'include'})
        let dataall = await resp.json()
        userSleep = dataall.current.time
        data = dataall["others"]
        console.log(dataall)
        console.log(data)
    })
</script>
<Scaffold>
    <Header slot="header">
        Leaderboard
    </Header>
    <Text tag="p" body>
        Your hours of sleep: {userSleep}
    </Text>
    <Text tag="p" subtitle>
        Others
    </Text>
    <Table>
        
        <TableHeader>
            <TableCell isHeader>Username</TableCell>
            <TableCell isHeader>Sleep per week</TableCell>
        </TableHeader>
       {#each data as user}
            <TableRow>
                    <TableCell>{user.username}</TableCell>
                    <TableCell>{user.time}</TableCell>
            </TableRow>
       {/each}
    </Table>
</Scaffold>