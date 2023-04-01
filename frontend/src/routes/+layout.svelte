<script>
	import Icon from '@iconify/svelte';
	import '../app.postcss';
	import { Modals, closeModal } from 'svelte-modals';
	import { SvelteToast } from '@zerodevx/svelte-toast';

	const options = {
		reversed: true,
		theme: {
			'--toastBackground': '#f3f5f6',
			'--toastBorder': '4px solid black',
			'--toastBoxShadow': '3px 3px 0 black',
			'--toastColor': 'black',
			'--toastBarBackground': '#a855f7'
		}
	};
</script>

<Modals>
	<!-- svelte-ignore a11y-click-events-have-key-events -->
	<div slot="backdrop" class="backdrop" on:click={closeModal} />
</Modals>

<SvelteToast {options} />

<div class="min-w-screen z-0 flex min-h-screen flex-col">
	<div class="container navbar mx-auto grow-0 justify-center bg-base-100">
		<div class="navbar-center">
			<a href="/" class="flex flex-row items-center gap-2">
				<img src="/vault-icon.png" alt="ChunkVault Vault Icon" class="w-10" />
				<div class="font-metropolis-black-italic text-2xl">ChunkVault</div>
				<div class="badge-primary badge badge-sm font-metropolis-semibold-italic">Lite</div>
			</a>
		</div>
	</div>

	<div class="container mx-auto min-h-full grow">
		<slot />
	</div>

	<div class="flex w-full grow-0 items-center justify-center p-6">
		<h1>
			Created with &hearts; by <a href="https://valink.io" target="_blank" rel="noopener noreferrer"
				>Valink Solutions</a
			>
		</h1>
	</div>
</div>

<style>
	:root {
		--toastContainerTop: auto;
		--toastContainerRight: 1.2rem;
		--toastContainerBottom: 1.2rem;
		--toastContainerLeft: auto;
	}
	.backdrop {
		position: fixed;
		top: 0;
		bottom: 0;
		right: 0;
		left: 0;
		z-index: 25;
		background: rgba(0, 0, 0, 0.5);
	}
</style>
