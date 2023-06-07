<script>
    export let selected_service = "";
</script>

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