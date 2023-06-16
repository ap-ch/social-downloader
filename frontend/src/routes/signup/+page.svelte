<script>

</script>

<svelte:head>
	<title>Sign up</title>
</svelte:head>

<div class="d-flex align-items-center py-4 bg-body-tertiary">
    <div class="w-30 m-auto">
        <form action="?/signup" method="POST"> 
            <h1 class="h3 mb-3 fw-normal">Sign up</h1>

            <div class="form-floating">
            <input name="email" type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
            <label for="floatingInput">Email address</label>
            </div>
            <div class="form-floating mt-3">
            <input name="password" type="password" class="form-control" id="floatingPassword" placeholder="Password">
            <label for="floatingPassword">Password</label>

            <button class="btn btn-primary w-100 py-10 mt-3" type="submit">Sign up</button>
        </form>
    </div> 
</div>