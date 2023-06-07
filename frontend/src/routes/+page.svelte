<script lang="ts">
	import type { PageServerData } from './$types';
	export let data: PageServerData;

	let user_info: any = null;

	if (data != null) {
		user_info = data["user_info"];
	}

	let selected_service = "";

	const setSelectedService = (service: string) => {
		selected_service = service;
		let serviceButtons;
		serviceButtons = document.getElementsByClassName("service-button");
		for (let serviceButton of serviceButtons) {
			serviceButton.classList.remove('btn-primary')
			serviceButton.classList.remove('text-white')
			serviceButton.classList.add('btn-outline-primary')
		}
		document.getElementById(`${service}-button`)?.classList.add('btn-primary')
		document.getElementById(`${service}-button`)?.classList.add('text-white')
		document.getElementById(`${service}-button`)?.classList.add('btn-lg')
		
	};

</script>

<svelte:head>
	<title>Home</title>
</svelte:head>

<body>

{#if user_info == null}
	<div class="text-center">
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
	</div>
{:else}
	<div style="background-color: #edededed; height: 90vh;">
		<div class="container px-4 py-3">
			<div class="row gx-3">
				<div class="col-3">
					<div class="p-3 bg-light rounded shadow-sm" style="height: 80vh;">
						<h3 class="text-center">Services</h3>
						<button id="telegram-button" class="container-fluid p-3 service-button btn btn-outline-primary" on:click={() => {setSelectedService('telegram'); return false;}} style="margin-bottom: 8px; text-align: left;">
							<h5 style="margin-bottom: 0px;"><i class="bi bi-telegram" style="margin-right: 8px"></i><span>Telegram<span></span></h5>
						</button>
						<button id="reddit-button" class="container-fluid p-3 service-button btn btn-outline-primary" on:click={() => {setSelectedService('reddit'); return false;}} style="margin-bottom: 8px; text-align: left;">
							<h5 style="margin-bottom: 0px;"><i class="bi bi-telegram" style="margin-right: 8px"></i><span>Reddit<span></span></h5>
						</button>
					</div>
				</div>
				<div class="col-6">
					<div class="p-3 bg-light rounded shadow-sm" style="height: 80vh;">
						{#if selected_service == ''}
							<div class="text-center">
								<h3><i class="bi bi-chat-square-dots"></i></h3>
								<p>Select a service on the left side bar to get started</p>
							</div>
						{:else}
							{#if selected_service == 'telegram'}
								<h3 class="text-center">Jobs</h3>
								<div class="container-fluid p-0">
									<div class="row gx-3">
										<div class="col-9">
											<div class="container-fluid p-3 border border-dark rounded" style="margin-bottom: 8px; text-align: left;">
												<h5 style="margin-bottom: 0px;"><span>Class<span></span></h5>
											</div>
										</div>
										<div class="col-3">
											<div class="container-fluid p-3 btn btn-outline-primary" style="margin-bottom: 8px; text-align: center;">
												<h5 style="margin-bottom: 0px;"><span>Download<span></span></h5>
											</div>
										</div>
									</div>
								</div>
							{/if}
						{/if}
					</div>
				</div>
				<div class="col-3">
					<div class="p-3 bg-light rounded shadow-sm" style="height: 80vh;">
						<div class="container-fluid h-100" style="overflow: scroll;">
							<div class="row">
								<h3 class="text-center">Features</h3>
							</div>
							{#if selected_service == 'telegram'}
								<div class="row">
									<div class="container-fluid p-3 btn btn-outline-primary" style="margin-bottom: 8px; text-align: left;">
										<h5 style="margin-bottom: 0px;"><span>Group<span></span></h5>
									</div>
								</div>
								<div class="row">
									<div class="container-fluid p-3 btn btn-outline-primary" style="margin-bottom: 8px; text-align: left;">
										<h5 style="margin-bottom: 0px;"><span>Channel<span></span></h5>
									</div>
								</div>
								<div class="row">
									<div class="container-fluid p-3 btn btn-outline-primary" style="margin-bottom: 8px; text-align: left;">
										<h5 style="margin-bottom: 0px;"><span>Messages<span></span></h5>
									</div>
								</div>
								<div class="row">
									<div class="container-fluid p-3 btn btn-outline-primary" style="margin-bottom: 8px; text-align: left;">
										<h5 style="margin-bottom: 0px;"><span>All Chats<span></span></h5>
									</div>
								</div>
								<div class="row">
									<div class="container-fluid p-3 btn btn-outline-primary" style="margin-bottom: 8px; text-align: left;">
										<h5 style="margin-bottom: 0px;"><span>Chat Details<span></span></h5>
									</div>
								</div>
								<div class="row">
									<div class="container-fluid p-3 btn btn-outline-primary" style="margin-bottom: 8px; text-align: left;">
										<h5 style="margin-bottom: 0px;"><span>My User<span></span></h5>
									</div>
								</div>
							{/if}
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
{/if}

</body>

<style>
</style>
