<script>
	import Icon from '@iconify/svelte';
	import '../app.postcss';
	import { Modals, closeModal } from 'svelte-modals'
	import { SvelteToast } from '@zerodevx/svelte-toast'

	const options = {
		theme: {
			'--toastContainerTop': 'auto',
			'--toastContainerBottom': '1.2rem',
			'--toastBackground': '#f3f5f6',
			'--toastBorder': '4px solid black',
			'--toastBoxShadow': '3px 3px 0 black',
			'--toastColor': 'black'
		}
	}
</script>

<Modals>
  <!-- svelte-ignore a11y-click-events-have-key-events -->
  <div
    slot="backdrop"
    class="backdrop"
    on:click={closeModal}
  />
</Modals>

<SvelteToast {options} />

<div class="flex flex-col min-h-screen min-w-screen z-0">

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

<style>
  .backdrop {
    position: fixed;
    top: 0;
    bottom: 0;
    right: 0;
    left: 0;
	z-index: 25;
    background: rgba(0,0,0,0.50)
  }
</style>
