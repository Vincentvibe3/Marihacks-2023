<script lang="ts">
    import { Header, Scaffold, Table, TableCell, TableHeader, TableRow } from 'nota-ui';
import type { PageData } from './$types';
    
    export let data: PageData;
</script>
<Scaffold>
    <Header slot="header">
        Leaderboards
    </Header>
    <Table>
        <TableHeader>
            <TableCell isHeader>Username</TableCell>
            <TableCell isHeader>Sleep per week</TableCell>
        </TableHeader>
        <TableRow>
            <TableCell isHeader>Example</TableCell>
            <TableCell isHeader>20</TableCell>
        </TableRow>
    </Table>
</Scaffold>