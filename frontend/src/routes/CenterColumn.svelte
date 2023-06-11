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
</script>

<div class="col-6 g-0" style="padding-right: 2vh">
    <div class="p-3 bg-light rounded shadow-sm" style="height: 80vh;">
        {#if selectedServiceValue == ""}
            <div class="text-center">
                <h3><i class="bi bi-chat-square-dots"></i></h3>
                <p>Select a service on the left side bar to get started</p>
            </div>
        {:else}
            {#if selectedServiceValue == "telegram"}
                <h3 class="text-center">Jobs</h3>
                <div class="container-fluid p-0">
                    <div class="row g-3">
                        <div class="col-9">
                            <div class="container-fluid p-3 border border-dark rounded" style="margin-bottom: 2vh; text-align: left;">
                                <h5 style="margin-bottom: 0px;"><span>Class<span></span></h5>
                            </div>
                        </div>
                        <div class="col-3">
                            <div class="container-fluid p-3 btn btn-outline-primary" style="margin-bottom: 2vh; text-align: center;">
                                <h5 style="margin-bottom: 0px;"><span>Download<span></span></h5>
                            </div>
                        </div>
                    </div>
                </div>
            {/if}
        {/if}
    </div>
</div>