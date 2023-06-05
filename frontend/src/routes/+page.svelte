<script lang="ts">
	import type { PageServerData } from './$types';
	export let data: PageServerData;

	let user_info: any = null;

	if (data != null) {
		user_info = data["user_info"];
	}
</script>

<svelte:head>
	<title>Home</title>
</svelte:head>

<div class="text-center">
	{#if user_info == null}
		<div class="container my-5">
			<div class="p-5 text-center bg-body-tertiary rounded-3">
			<h1 class="text-body-emphasis">Social Downloader</h1>
			<p class="col-lg-8 mx-auto fs-5 text-muted">
				Easily download content from multiple social networks
			</p>
			<div class="d-inline-flex gap-2 mb-5">
				<a href="/signup" class="d-inline-flex align-items-center btn btn-primary btn-lg px-4 rounded-pill" type="button">
				Create an account
				</a>
				<a href="/login" class="btn btn-outline-secondary btn-lg px-4 rounded-pill" type="button">
				Log in
				</a>
			</div>
			</div>
		</div>
	{:else}
		<h1>Social Downloader</h1>
	{/if}
</div>

