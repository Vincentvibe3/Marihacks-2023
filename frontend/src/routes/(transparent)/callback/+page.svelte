<script lang="ts">
	import { page } from '$app/stores';
	import { onMount } from 'svelte';
  
	  onMount(()=>{
		  let loggedIn = $page.url.searchParams.get('loggedIn') ? true : false
		  document.cookie = `loggedIn=${loggedIn}`; 
		  if (loggedIn){
			document.location.href = "/"
		  } else {
			document.location.href = "/home"
		  }
		  
	  })
  </script>