<script>
	// @ts-nocheck
	import { page } from '$app/stores';
</script>

<div class="flex h-full w-full flex-col items-center justify-center font-metropolis text-lg">
	<h1 class="font-metropolis-semibold text-2xl">{$page.status}</h1>
	<p>{$page.error.message}</p>
</div>
