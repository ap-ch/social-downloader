<script lang="ts">
    import logo from '$lib/images/logo.png';
    export let user_info: any | null;
</script>

  <nav class="navbar navbar-expand-sm navbar-light bg-light" aria-label="Sixth navbar example">
    <div class="container-fluid">
      <a href="/">
        <img alt="Social Downloader" src={logo} style="width: 200px; vertical-align: middle;"/>
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarsExample06" aria-controls="navbarsExample06" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarsExample06">
        <ul class="navbar-nav me-auto mb-2 mb-xl-0"></ul>
        <ul class="navbar-nav ml-auto">
          {#if user_info != null}
            <li class="nav-item">
              <p class="navbar-text" style="margin-right: 8px">Welcome, {user_info["email"]}</p> 
            </li>
          {/if}
          <li class="nav-item">
            {#if user_info == null}
              <a href="/login" class="btn btn-outline-dark me-2">Log in</a>
            {:else}
              <a href="/logout" class="btn btn-outline-dark me-2">Log out</a>
            {/if}
          </li>
          <li class="nav-item">
            <a href="/signup" class="btn btn-outline-dark me-2">Sign up</a>
          </li>
      </div>
    </div>
  </nav>