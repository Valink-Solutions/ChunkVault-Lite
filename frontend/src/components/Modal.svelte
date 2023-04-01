<script lang="ts">
	import { closeModal } from 'svelte-modals';

	export let isOpen: Boolean;

	export let title: String;

	export let message: String;

	export let onConfirm: () => void;
</script>

{#if isOpen}
	<div
		role="dialog"
		class="card absolute top-1/2 left-1/2 z-30 min-w-[400px] -translate-x-1/2 -translate-y-1/2 transform bg-base-100"
	>
		<div class="card-body">
			<h2 class="card-title">{title}</h2>
			<p>{message}</p>
			<div class="card-actions justify-between md:justify-end">
				<button on:click={closeModal} class="btn-ghost btn">Close</button>
				<button on:click={onConfirm} class="btn-primary btn">Confirm</button>
			</div>
		</div>
	</div>
{/if}
