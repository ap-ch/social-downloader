<script lang="ts">
	import { userInfo, services, selectedService } from './stores';

    let userInfoValue: any;
	let servicesValue: any;
	let selectedServiceValue: any;

	userInfo.subscribe(value => {
		userInfoValue = value;
	});

	services.subscribe(value => {
		servicesValue = value;
	});

	selectedService.subscribe(value => {
		selectedServiceValue = value;
	});

    const getServiceFeatures = (service: string) => {
        return servicesValue[service].features
    };
</script>

<div class="col-3 g-0">
    <div class="p-3 bg-light rounded shadow-sm" style="height: 80vh;">
        <div class="row">
            <h3 class="text-center">Features</h3>
        </div>
        <div class="container-fluid scrollable" style="height: 95%;">
            {#if servicesValue != null && selectedServiceValue != ""}
                {#each getServiceFeatures(selectedServiceValue) as feature}
                    <div class="row">
                        <div class="container-fluid p-3 btn btn-outline-primary" style="margin-bottom: 8px; text-align: left;">
                            <h5 style="margin-bottom: 0px;"><span>{feature[Object.keys(feature)[0]].name}<span></span></h5>
                        </div>
                    </div>
                {/each}
            {/if}
        </div>
    </div>
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