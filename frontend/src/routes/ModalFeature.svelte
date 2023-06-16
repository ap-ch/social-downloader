<script lang="ts">
	import { userPrefs, services, selectedService, okShowFeatureModal, selectedFeatureName} from './stores';

    export let selectedFeature: any;

    let selectedAuthMethod: string = "";

	let dialog: any; // HTMLDialogElement

    let userPrefsValue: any;
	let servicesValue: any;
	let selectedServiceValue: any;

    let okShowFeatureModalValue: any;

    userPrefs.subscribe(value => {
		userPrefsValue = value;
	});

	services.subscribe(value => {
		servicesValue = value;
	});

	selectedService.subscribe(value => {
		selectedServiceValue = value;
	});

    okShowFeatureModal.subscribe(value => {
        selectedAuthMethod = "";
		okShowFeatureModalValue = value;
	});

	const getFeatureParameters = (serviceFeature: any) => {
		let parameters: any = [];
		try {
			parameters = Object.entries(serviceFeature.parameters);
		}
		finally {
			return parameters
		}
    }

    const isParamRequired = (parameter: any) => {
		let isRequired: boolean = false;
		try {
			isRequired = parameter.required;
		}
		finally {
			return isRequired
		}
    }

	const handleRequestFeature = async (event: any) => {
		let formData = new FormData(event.target);
		let requestData: any = Object.fromEntries(formData.entries());
		for (let [requestItem, requestItemValue] of Object.entries(requestData)) {
			if (requestItemValue == "") {
				delete requestData[requestItem];
			}
		}
		let requestParams = new URLSearchParams(requestData).toString();
		let params = `?res=/${selectedServiceValue}${selectedFeature.path}&${requestParams}`
		console.log(`using ${params}`)
		await fetch(`/api/redirect-server${params}`, 
			{
				method: "get",
			}
		);
		dialog.close();
		let oldServiceValue = selectedServiceValue;
		selectedService.set("");
		selectedService.set(oldServiceValue);
	}

	$: if (selectedServiceValue) {
		selectedFeatureName.set("")
	}
	
	$: if (dialog && okShowFeatureModalValue) {
        dialog.showModal();
    }

</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
{#if selectedFeature}
<dialog bind:this={dialog} on:close={() => (okShowFeatureModal.set(false))}>
    <button class="btn btn-outline-dark" on:click={() => {dialog.close(); return false;}} style="margin-top: 3%; margin-left: 87%; border-radius: 10px; height: 37px;">X</button>
	<div class="text-center" on:click|stopPropagation>
        <h2>
            {selectedFeature.name}
        </h2>
        <p>{selectedFeature.description}</p>
        <div class="d-flex align-items-center py-4 bg-body-tertiary" style="min-width: 20em;">
            <div class="w-30 m-auto">
                <form on:submit|preventDefault={(event) => {handleRequestFeature(event); return false;}} method="POST">
                    {#each getFeatureParameters(selectedFeature) as parameter}
                        {#if isParamRequired(parameter[1])}
                            <div class="form-floating" style="margin-bottom: 1rem;">
                                <input name={parameter[0]} type={parameter[1].type} class="form-control" id="floatingInput" required>
                                <label for="floatingInput">{parameter[1].name} <span class="text-danger">*</span></label>
                            </div>
                        {:else}
                            <div class="form-floating">
                                <input name={parameter[0]} type={parameter[1].type} class="form-control" id="floatingInput">
                                <label for="floatingInput">{parameter[1].name}</label>
                            </div>
                        {/if}
                    {/each}
                    <button class="btn btn-primary w-100 py-10 mt-3" type="submit">Submit Request</button>
                </form>
            </div> 
        </div>
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