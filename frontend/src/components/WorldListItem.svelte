<script lang="ts">
	import { formatBytes, formatDifficulty } from '../utils/reusables';
	import { openModal, closeModal } from 'svelte-modals';
	import Modal from './Modal.svelte';
	import { goto } from '$app/navigation';
	import type { World } from '../utils/schemas';
	export let world: World;

	function handleClick() {
		openModal(Modal, {
			title: 'Delete World.',
			message: `This will delete world: ${world.name}, and make it unrecoverable.`,
			onConfirm: async () => {
				await fetch(`/api/worlds/${world.key}`, {
					method: 'DELETE'
				});

				goto(`/worlds`, { replaceState: true, invalidateAll: true });

				closeModal();
			}
		});
	}
</script>

<div class="card card-side w-full bg-base-100">
	<div class="flex pl-6 md:items-start md:pt-7">
		<figure class="drop-shadow-neu">
			<img class="h-[82px] w-[82px] border-4 border-black" src={world.image} alt={world.name} />
		</figure>
	</div>
	<div class="card-body justify-center">
		<div class="flex flex-row items-center justify-between">
			<h1 class="card-title">{world.name}</h1>
			{#if world.is_public}
				<span class="badge-accent badge badge-sm">Public</span>
			{:else}
				<span class="badge-ghost badge badge-sm">Private</span>
			{/if}
		</div>

		<div>
			<div class="flex flex-col md:flex-row">
				<h2 class="card-subtitle">
					Difficulty: {formatDifficulty(world.difficulty)}
				</h2>
				<div class="hidden md:divider md:divider-horizontal" />
				<h2 class="card-subtitle">
					World Size: {formatBytes(world.size)}
				</h2>
			</div>
			<div class="flex w-fit flex-col md:flex-row">
				<h2 class="card-subtitle">Seed: {world.seed}</h2>
				<div class="hidden md:divider md:divider-horizontal" />
				<h2 class="card-subtitle">Snapshots: {world.num_snapshots}</h2>
			</div>
		</div>

		<div class="card-actions justify-center md:justify-end">
			<a href={`/worlds/${world.key}`} class="btn-primary btn-sm btn">View</a>
			<a href="/" class="btn-disabled btn-secondary btn-sm btn">Share</a>
			<button on:click={handleClick} class="btn-error btn-sm btn">Delete</button>
		</div>
	</div>
</div>
