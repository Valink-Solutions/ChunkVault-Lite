<script>
	import Icon from '@iconify/svelte';
	import '../app.postcss';
</script>

<div class="flex flex-col min-h-screen min-w-screen">

	<div class="grow-0 navbar bg-base-100 container mx-auto justify-center">
		<div class="navbar-center">
			<a href="/" class="flex flex-row gap-2 items-center">
				<img src="/vault-icon.png" alt="ChunkVault Vault Icon" class="w-10">
				<div class="font-metropolis-black-italic text-2xl">ChunkVault</div>
				<div class="font-metropolis-semibold-italic badge badge-primary badge-sm">Lite</div>
			</a>
		</div>
	</div>

	<div class="grow container mx-auto min-h-full">
		<slot />
	</div>

	<div class="grow-0 flex w-full justify-center items-center p-6">
		<h1>Created with &hearts; by <a href="https://valink.io" target="_blank" rel="noopener noreferrer">Valink Solutions</a></h1>
	</div>
</div>
