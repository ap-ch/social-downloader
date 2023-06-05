<script lang="ts">
    import Header from "./Header.svelte";
	import Footer from "./Footer.svelte"
	import type { PageServerData } from './$types';
	export let data: PageServerData;

	let user_info: any | null = null;

	if (data != null) {
		user_info = data["user_info"];
	}
</script>

<div>
	<Header user_info={user_info}/>

	<main>
		<slot/>
	</main>

	<Footer/>
</div>
