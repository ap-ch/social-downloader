<script lang="ts">
	import { userInfo, services, selectedService, selectedFeatureName, okShowFeatureModal} from './stores';

    let userInfoValue: any;
	let servicesValue: any;
	let selectedServiceValue: any;
    let selectedFeatureNameValue: any;

	userInfo.subscribe(value => {
		userInfoValue = value;
	});

	services.subscribe(value => {
		servicesValue = value;
	});

	selectedService.subscribe(value => {
		selectedServiceValue = value;
	});

    selectedFeatureName.subscribe(value => {
		selectedFeatureNameValue = value;
	});

    const getFeatureDetail = (feature: any) => {
		let detail: any = "";
		try {
            let detailText: any;
            detailText = feature[Object.keys(feature)[0]].detail;
            if (detailText) {
                detail = detailText;
            }
		}
		finally {
			return detail
		}
    }

    const getServiceFeatures = (service: string) => {
        return servicesValue[service].features
    };

    const setSelectedFeature = (featureName: string) => {
        selectedFeatureName.set(featureName);
        okShowFeatureModal.set(true);
    }
</script>

<div class="col-3 g-0">
    <div class="p-3 bg-light rounded shadow-sm" style="height: 80vh;">
        <div class="row">
            <h3 class="text-center">Features</h3>
        </div>
        <div class="container-fluid scrollable" style="height: 95%;">
            {#if servicesValue != null && selectedServiceValue != ""}
                {#key selectedServiceValue}
                    {#each getServiceFeatures(selectedServiceValue) as feature}
                        <div class="row">
                            <button class="container-fluid p-3 btn btn-outline-primary" on:click={() => {setSelectedFeature(Object.keys(feature)[0]) ;return false;}} style="margin-bottom: 8px; text-align: left;">
                                <h5 style="margin-bottom: 0px;"><span>{feature[Object.keys(feature)[0]].name}</span> <small class="opacity-75">{getFeatureDetail(feature)}</small></h5>
                            </button>
                        </div>
                    {/each}
                {/key}
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