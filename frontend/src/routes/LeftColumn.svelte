<script lang="ts">
    import { userInfo, services, selectedService } from './stores';

    let userInfoValue: any;
    let servicesValue: any;
    let serviceEntries: any;
    let selectedServiceValue: any;

    userInfo.subscribe(value => {
        userInfoValue = value;
    });

    services.subscribe((value: any) => {
        servicesValue = value;
        serviceEntries = Object.entries(value);
    });

    selectedService.subscribe(value => {
        selectedServiceValue = value;
    });

    const setSelectedService = (service: string) => {
		selectedService.set(service);
		let serviceButtons;
		serviceButtons = document.getElementsByClassName("service-button");
		for (let serviceButton of serviceButtons) {
			serviceButton.classList.remove('btn-primary');
			serviceButton.classList.remove('text-white');
			serviceButton.classList.add('btn-outline-primary');
		}
		document.getElementById(`${service}-button`)?.classList.add('btn-primary');
		document.getElementById(`${service}-button`)?.classList.add('text-white');
	};

    const getServiceAuthentication = (service: string) => {
        let currentService = servicesValue[service];
        if (currentService != null) {
            if ("authentication" in currentService) {
                return currentService.authentication
            }
            else {
                return null
            }
        }
    }
</script>

<div class="col-3 g-0" style="padding-right: 2vh">
    <div class="p-3 bg-light rounded shadow-sm" style="height: 70vh;">
        <div class="row">
            <h3 class="text-center">Services</h3>
        </div>
        <div class="container-fluid scrollable" style="height: 95%;">
            {#each serviceEntries as serviceEntry}
                <div class="row">
                    <button id="{serviceEntry[0]}-button" class="container-fluid p-3 service-button btn btn-outline-primary" on:click={() => {setSelectedService(serviceEntry[0]); return false;}} style="margin-bottom: 8px; text-align: left;">
                        <h5 style="margin-bottom: 0px;"><i class="bi bi-{serviceEntry[1].icon}" style="margin-right: 8px"></i><span>{serviceEntry[1].name}<span></span></h5>
                    </button>
                </div>
            {/each}
        </div>
    </div>
    {#if getServiceAuthentication(selectedServiceValue) != null}
        <div class="bg-light rounded shadow-sm" style="height: 8vh; margin-top: 2vh;">
            <button class="container-fluid p-3 btn btn-outline-primary shadow-sm text-center" on:click={() => {}} style="text-align: left; height: 100%;">
                <h5 style="margin-bottom: 0px;"><i class="bi bi-key" style="margin-right: 8px"></i><span>Service Authentication<span></span></h5>
            </button>
        </div>
    {:else}
        <div class="bg-light rounded shadow-sm" style="height: 8vh; margin-top: 2vh;">
            <button disabled class="container-fluid p-3 btn btn-disabled shadow-sm text-center" on:click={() => {}} style="text-align: left; height: 100%;">
                <h5 style="margin-bottom: 0px;"><i class="bi bi-key" style="margin-right: 8px"></i><span>Service Authentication<span></span></h5>
            </button>
        </div>
    {/if}
</div>

<style>
    .scrollable {
        overflow: scroll;
        -ms-overflow-style: none;  /* Internet Explorer 10+ */
        scrollbar-width: none;  /* Firefox */
    }
    .scrollable::-webkit-scrollbar { 
        display: none;  /* Safari and Chrome */
    }
</style>