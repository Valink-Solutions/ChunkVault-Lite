<script lang="ts">
	import { closeModal } from 'svelte-modals';
	import type { World } from '../utils/schemas';
	import { goto } from '$app/navigation';

	export let isOpen: boolean;

	export let title: string;

	export let world: World;

	let error: string | undefined;

	export let onConfirm: Function;

	async function updateWorld() {
		try {
			const response = await fetch(`/api/worlds/${world.key}`, {
				method: 'PATCH',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify({
					name: world.name,
					seed: world.seed,
					is_public: world.is_public
				})
			});

			if (!response.ok) {
				throw new Error('An error occurred while updating the world. Try again later.');
			}

			onConfirm();
		} catch (error) {
			console.error(error);
		}
	}
</script>

{#if isOpen}
	<div
		role="dialog"
		class="card absolute top-1/2 left-1/2 z-30 min-w-[400px] -translate-x-1/2 -translate-y-1/2 transform bg-base-100"
	>
		<div class="card-body">
			<h2 class="card-title font-metropolis-black-italic">Editing: {title}</h2>

			{#if error}
				<div class="alert alert-error shadow-lg">
					<div>
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-6 w-6 flex-shrink-0 stroke-current"
							fill="none"
							viewBox="0 0 24 24"
							><path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
							/></svg
						>
						<span>{error}</span>
					</div>
				</div>
			{/if}

			<form action="" class="flex flex-col gap-2">
				<div class="form-control w-full">
					<label for="name" class="label justify-between gap-2.5">
						<span class="label-text">World Name:</span>
					</label>
					<input
						name="name"
						type="text"
						bind:value={world.name}
						class="input-bordered input-primary input w-full max-w-sm"
					/>
				</div>
				<div class="form-control w-full">
					<label for="seed" class="label justify-between gap-2.5">
						<span class="label-text">World Seed:</span>
					</label>
					<input
						name="seed"
						type="text"
						bind:value={world.seed}
						class="input-bordered input-primary input w-full max-w-sm"
					/>
				</div>
				<div class="form-control">
					<label class="label cursor-pointer">
						<span class="label-text">Public Visibility</span>
						<input type="checkbox" class="toggle rounded-none" bind:checked={world.is_public} />
					</label>
				</div>
			</form>

			<p class="max-w-xs text-center font-metropolis">
				Changing these values <strong class="font-metropolis-semibold">WILL NOT</strong> reflect on the
				actual world.
			</p>

			<div class="card-actions w-full justify-between">
				<button on:click={closeModal} class="btn-ghost btn">Close</button>
				<button on:click={updateWorld} class="btn-primary btn">Update</button>
			</div>
		</div>
	</div>
{/if}
