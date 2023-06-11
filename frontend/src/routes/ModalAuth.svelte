<script lang="ts">
	import { userPrefs, services, selectedService, okShowAuthModal, okCloseAuthModal} from './stores';

    export let authentication: any;

    let selectedAuthMethod: string = "";
	let is2fa: boolean = false;

	let dialog: any; // HTMLDialogElement

    let userPrefsValue: any;
	let servicesValue: any;
	let selectedServiceValue: any;

    let okShowAuthModalValue: any;
	let okCloseAuthModalValue: any;

    userPrefs.subscribe(value => {
		userPrefsValue = value;
	});

	services.subscribe(value => {
		servicesValue = value;
	});

	selectedService.subscribe(value => {
		selectedServiceValue = value;
	});

    okShowAuthModal.subscribe(value => {
        selectedAuthMethod = "";
		okShowAuthModalValue = value;
	});

	okCloseAuthModal.subscribe(value => {
		okCloseAuthModalValue = value;
	});

	const getAuthMethod = (method: string) => {
		let auth_method: any;
        for (var i = 0; i < authentication.length; i++) {
			if (Object.keys(authentication[i]).includes(method)) {
				auth_method = authentication[i][method];
			}
		}
		return auth_method;
    }

	const getAuthMethodPath = (auth_method: any) => {
		let path: any = "";
		try {
			path = auth_method.path;
		}
		finally {
			return path
		}
    }

	const getAuthMethodParameters = (auth_method: any) => {
		let parameters: any = [];
		try {
			parameters = Object.entries(auth_method.parameters);
		}
		finally {
			return parameters
		}
    }

	const hasAuthMethod2fa = (auth_method: any) => {
		let has2fa: boolean = false;
		try {
			has2fa = auth_method["2fa"];
		}
		finally {
			return has2fa
		}
    }

	const handleServiceAuthenticate = async (event: any) => {
		let success = await serviceAuthenticate(event);
		if (success && !is2fa) {
			dialog.close();
		}
	}

	const handleServiceVerify = async (event: any) => {
		let success = await serviceVerify(event);
		if (success) {
			dialog.close();
		}
	}

	const serviceAuthenticate = async (event: any) => {
		const formData = new FormData(event.target);
		const authData = Object.fromEntries(formData.entries());
		let params = `?res=/preferences/${selectedServiceValue}_login`
		let response = await fetch(`/api/redirect-server${params}`, 
			{
				method: "post",
				headers: {
					"Content-Type": "application/json"
				},
				body: JSON.stringify(authData)
			}
		);
		if (response.ok) {
			let auth_method = getAuthMethod(selectedAuthMethod);
			let auth_method_path = getAuthMethodPath(auth_method);
			params = `?res=/${selectedServiceValue}${auth_method_path}`
			let response_login = await fetch(`/api/redirect-server${params}`, 
				{
					method: "get"
				}
			);
			if (response_login.ok) {
				if (hasAuthMethod2fa(auth_method)) {
					is2fa = true;
				}
				return true;
			}
			else {
				return false;
			}
		}
		else {
			return false;
		}
	}

	const serviceVerify = async (event: any) => {
		const formData = new FormData(event.target);
		const verificationCode = Object.fromEntries(formData.entries()).code;
		let auth_method_path = getAuthMethodPath(getAuthMethod(selectedAuthMethod));
		const params = `?res=/${selectedServiceValue}${auth_method_path}?code=${verificationCode}`
		const response = await fetch(`/api/redirect-server${params}`,
			{
				method: "get"
			}
		);
		if (response.ok) {
			is2fa = false;
			return true;
		}
		else {
			return false
		}
	}

	$: if (dialog && authentication != null) {
        dialog.addEventListener('cancel', (event: any) => {
            event.preventDefault();	
        });
        dialog.showModal();
    }

	$: console.log(authentication)
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
{#if authentication != null && (userPrefsValue == null || !(`${selectedServiceValue}_login` in userPrefsValue))}
<dialog bind:this={dialog} on:close={() => (okShowAuthModal.set(false))}>
	<div class="text-center" on:click|stopPropagation>
        {#if selectedAuthMethod == ""}
            <h2>
                Select Authentication Mode
            </h2>
            <span>This service requires authentication to be used.<br>Please, select one of the following methods:</span>
            {#each authentication as auth_method}
                <div class="container-fluid btn btn-outline-primary" on:click={() => {selectedAuthMethod = Object.keys(auth_method)[0]}} style="margin-top: .5rem;">
                    {auth_method[Object.keys(auth_method)[0]].name}
                </div>
            {/each}
        {:else}
			{#if !is2fa}
				<h2>
					Authentication
				</h2>
				<div class="d-flex align-items-center py-4 bg-body-tertiary">
					<div class="form-signin w-30 m-auto">
						<form on:submit|preventDefault={(event) => {handleServiceAuthenticate(event); return false;}} method="POST">
							{#each getAuthMethodParameters(getAuthMethod(selectedAuthMethod)) as parameter}
								{#if parameter[1].required}
									<div class="form-floating">
										<input name={parameter[0]} type={parameter[1].type} class="form-control" id="floatingInput" required>
										<label for="floatingInput">{parameter[1].name}</label>
									</div>
								{:else}
									<div class="form-floating">
										<input name={parameter[0]} type={parameter[1].type} class="form-control" id="floatingInput">
										<label for="floatingInput">{parameter[1].name}</label>
									</div>
								{/if}
							{/each}
							<button class="btn btn-primary w-100 py-10 mt-3" type="submit">Authenticate</button>
						</form>
					</div> 
				</div>
				{:else}
					<h2>
						Verification
					</h2>
					<div class="d-flex align-items-center py-4 bg-body-tertiary">
						<div class="form-signin w-30 m-auto">
							<form on:submit|preventDefault={(event) => {handleServiceVerify(event); return false;}} method="POST">
								<div class="form-floating">
									<input name="code" type="text" class="form-control" id="floatingInput" required>
									<label for="floatingInput">Code</label>
								</div>
								<button class="btn btn-primary w-100 py-10 mt-3" type="submit">Verify</button>
							</form>
						</div> 
					</div>
			{/if}
        {/if}
	</div>
</dialog>
{/if}

<style>
	dialog {
		max-width: 32em;
		border-radius: 0.2em;
		border: none;
		padding: 0;
	}
	dialog::backdrop {
		background: rgba(0, 0, 0, 0.3);
	}
	dialog > div {
		padding: 1em;
	}
	dialog[open] {
		animation: zoom 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
	}
	@keyframes zoom {
		from {
			transform: scale(0.95);
		}
		to {
			transform: scale(1);
		}
	}
	dialog[open]::backdrop {
		animation: fade 0.2s ease-out;
	}
	@keyframes fade {
		from {
			opacity: 0;
		}
		to {
			opacity: 1;
		}
	}
</style>