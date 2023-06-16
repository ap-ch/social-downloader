<script lang="ts">
	import LeftColumn from './LeftColumn.svelte';
	import CenterColumn from './CenterColumn.svelte';
	import RightColumn from './RightColumn.svelte';
	import ModalAuth from './ModalAuth.svelte';

	import { userInfo, services, selectedService, okShowAuthModal, okShowFeatureModal, userPrefs, selectedFeatureName} from './stores';
	import type { PageServerData } from './$types';
    import ModalFeature from './ModalFeature.svelte';
	export let data: PageServerData;

	if (data != null) {
		userInfo.set(data.userInfo);
		userPrefs.set(data.userPrefs);
		services.set(data.services);
	}

	let userInfoValue: any;
	let servicesValue: any;
	let selectedServiceValue: any;
	let selectedFeatureNameValue: any;

	let okShowAuthModalValue: any
	let okShowFeatureModalValue: any

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

	okShowAuthModal.subscribe(value => {
		okShowAuthModalValue = value;
	});

	okShowFeatureModal.subscribe(value => {
		okShowFeatureModalValue = value;
	});

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

	let serviceFeatures: any;

	$: serviceFeatures = getServiceFeatures(selectedServiceValue);

	const getServiceFeatures = (service: string) => {
		let serviceFeatures: any = null;
		if (servicesValue && service) {
			serviceFeatures = servicesValue[service].features;
		}
		return serviceFeatures;
    };

    const getServiceFeature = (feature: string) => {
		let serviceFeature: any;
		if (serviceFeatures != null) {
			for (var i = 0; i < serviceFeatures.length; i++) {
				if (Object.keys(serviceFeatures[i]).includes(feature)) {
					serviceFeature = serviceFeatures[i][feature];
				}
			}
		}
		return serviceFeature;
    }

</script>

<svelte:head>
	<title>Home</title>
</svelte:head>

<body>

{#if userInfoValue == null}
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
	{#if okShowAuthModalValue}
		<ModalAuth authentication={getServiceAuthentication(selectedServiceValue)}/>
	{/if}
	{#if okShowFeatureModal && serviceFeatures}
		<ModalFeature selectedFeature={getServiceFeature(selectedFeatureNameValue)}/>
	{/if}
	<div style="background-color: #edededed; height: 90vh;">
		<div class="container py-3">
			<div class="row">
				<LeftColumn/>
				<CenterColumn/>
				<RightColumn/>
			</div>
		</div>
	</div>
{/if}
</body>
