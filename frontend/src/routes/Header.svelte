<script lang="ts">
    import logo from '$lib/images/logo.png';
    import { userInfo } from './stores';

    let userInfoValue: any;

    userInfo.subscribe(value => {
        userInfoValue = value;
    });
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
        {#if userInfoValue != null}
          <span class="navbar-text" style="margin-right: 8px">Welcome, {userInfoValue.email}</span> 
        {/if}
          {#if userInfoValue == null}
            <li class="nav-item">
              <a href="/login" class="btn btn-outline-dark me-2">Log in</a>
            </li>
            <li class="nav-item">
              <a href="/signup" class="btn btn-outline-dark me-2">Sign up</a>
            </li>
          {:else}
            <li class="nav-item">
              <a href="/logout" class="btn btn-outline-dark me-2">Log out</a>
            </li>
          {/if}
    </div>
  </div>
</nav>