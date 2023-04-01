<script lang="ts">
    import { Header, Scaffold, Table, TableCell, TableHeader, TableRow } from 'nota-ui';
import type { PageData } from './$types';
    
    export let data: PageData;
    let weeksum = []
    let username = []
    async function getData(url="") {
        const response = await fetch(url)
        let data = await response.json()
        for(let User of data){
            username.push(User.username)
            weeksum.push(User.weeksum)
        }
        return response.json()
    }
</script>
<Scaffold>
    <Header slot="header">
        Leaderboards
    </Header>
    <Table>
        <TableHeader>
            <TableCell isHeader>usernames</TableCell>
            <TableCell isHeader>Sleep per week</TableCell>
        </TableHeader>
        <TableRow>
            <TableCell isHeader>{usernames}</TableCell>
            <TableCell isHeader>{weeksum}</TableCell>
        </TableRow>
    </Table>
</Scaffold>