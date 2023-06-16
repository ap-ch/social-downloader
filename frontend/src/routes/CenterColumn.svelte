<script lang="ts">
	import { userInfo, services, selectedService } from './stores';

    let userInfoValue: any;
	let servicesValue: any;
	let selectedServiceValue: any;
    let serviceTasks: any = [];
    let completedTaskIds: any = [];

	userInfo.subscribe(value => {
		userInfoValue = value;
	});

	services.subscribe(value => {
		servicesValue = value;
	});

	selectedService.subscribe(async (value) => {
		selectedServiceValue = value;
        serviceTasks = [];
        if (selectedServiceValue) {
            completedTaskIds = [];
            refresh();
        }
	});

    let refresh = async () => {
        await refreshJobs();
        await refreshJobStatus();
    }

    let refreshJobs = async () => {
        if (selectedServiceValue) {
            let params = `?res=/tasks/&task_type=${selectedServiceValue}`;
            let response = await fetch(`/api/redirect-server${params}`, 
                {
                    method: "get"
                }
            );
            if (response.ok) {
                serviceTasks = await response.json();
            }
            else {
                serviceTasks = [];
            }
        }
    };

    let refreshJobStatus = async () => {
        if (serviceTasks.length > 0) {
            serviceTasks.forEach(async (serviceTask: any) => {
                if (!(completedTaskIds.includes(serviceTask["task_id"]))) {
                    let params = `?res=/results/${selectedServiceValue}/${serviceTask["task_id"]}`;
                    let response = await fetch(`/api/redirect-server${params}`, 
                        {
                            method: "get"
                        }
                    );
                    if (response.ok) {
                        let res_task_result = await response.json();
                        if (!(`status` in res_task_result)) {
                            let task_button: any = document.getElementById(`task-button-${serviceTask["task_id"]}`);
                            task_button.disabled = false;
                            task_button.innerHTML = '<h5 style="margin-bottom: 0px;"><i class="bi bi-download"></i></h5>';
                            task_button?.classList.remove('btn-disabled');
                            task_button?.classList.add('btn-outline-primary');
                            completedTaskIds = completedTaskIds.concat(serviceTask["task_id"]);
                        }
                    }
                }
            });
        }
    };

    $: if (serviceTasks.length > 0) {
        clearInterval(interval);
        interval = setInterval(refresh, 5000);
    }
    else {
        clearInterval(interval);
        interval = setInterval(refresh, 10000);
    }

    let interval = setInterval(refresh, 10000);

    let downloadResult = async (task_id: string, task_detail: string) => {   
        let params = `?res=/results/${selectedServiceValue}/${task_id}`;
        fetch(`/api/redirect-server${params}`, 
            {
                method: "get"
            }
        )
        .then(async(response) => {
            return response.json()
        })
        .then(json => {
            var data = "text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(json, null, 4));
            let a = document.createElement('a');
            a.href = "data:" + data;
            let today = new Date();
            let todayText = today.toISOString().replaceAll(":", "-").slice(0, 19)
            a.download = `${selectedServiceValue}-${task_detail}-result-${todayText}.json`;
            a.click();
        })
        .catch(function(err) {
            console.error(err);
        })
    }

    let deleteTask = async (task_id: string) => {
        let params = `?res=/tasks/delete/${task_id}`;
        let response = await fetch(`/api/redirect-server${params}`, 
            {
                method: "get"
            }
        );
        if (response.ok) {
            let oldServiceValue = selectedServiceValue;
            selectedService.set("");
            selectedService.set(oldServiceValue);
        }
    }
</script>

<div class="col-6 g-0" style="padding-right: 2vh">
    <div class="p-3 bg-light rounded shadow-sm" style="height: 80vh; text-align:center;">
            {#if selectedServiceValue == ""}
                <div class="text-center">
                    <h3><i class="bi bi-chat-square-dots"></i></h3>
                    <p>Select a service on the left side bar to get started</p>
                </div>
            {:else}
                <div class="row">
                    <h3 class="text-center">Requests</h3>
                </div>
                {#if serviceTasks.length == 0}
                    <h5>Your content requests for <code>{selectedServiceValue}</code> are loading...</h5>
                    <h6>Don't have any? Try making your first request with the right side bar.</h6>
                    <span class="spinner-border text-primary" style="margin:auto;"></span>
                {/if}
                    <div class="container-fluid scrollable" style="height: 95%;">
                        {#each serviceTasks as serviceTask, i}
                            <div id="task-row-{serviceTask["task_id"]}" class="row g-1">
                                <div class="col-4">
                                    <div title={serviceTask["task_detail"]} class="container-fluid p-3 border border-dark rounded text-truncate" style="margin-bottom: 8px; text-align: left;">
                                        <span>{i+1}. <code>{serviceTask["task_detail"]}</code></span>
                                    </div>
                                </div>
                                <div class="col-4">
                                    <div class="container-fluid p-3 border border-dark rounded text-center" style="margin-bottom: 8px; text-align: left; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                                        <span style="margin-bottom: 0px;">{serviceTask["date_created"].replace("T", " ").slice(0, 19)}</span>
                                    </div>
                                </div>
                                <div class="col-2">
                                    <button class="container-fluid p-3 btn btn-outline-danger" on:click={async () => {deleteTask(serviceTask["task_id"]); return false;}} style="margin-bottom: 8px; text-align: center;">
                                        <h5 style="margin-bottom: 0px;"><i class="bi bi-trash3-fill"></i></h5>
                                    </button>
                                </div>
                                <div class="col-2">
                                    <button disabled id="task-button-{serviceTask["task_id"]}" on:click={async () => {downloadResult(serviceTask["task_id"], serviceTask["task_detail"]); return false;}} class="container-fluid p-3 btn btn-disabled" style="margin-bottom: 8px; text-align: center;">
                                        <h5 style="margin-bottom: 0px;"><i class="bi bi-hourglass"></i></h5>
                                    </button>
                                </div>
                            </div>
                        {/each}
                    </div>
            {/if}
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