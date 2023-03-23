<script lang="ts">
	import WorldSnapshotList from '../../../components/WorldSnapshotList.svelte';
	import type { PageData } from '../../../routes/$types';
	import { formatBytes, formatDifficulty } from '../../../utils/reusables';
	import { openModal, closeModal } from 'svelte-modals';
	import Modal from '../../../components/Modal.svelte';
	import { goto } from '$app/navigation';
	import type { World, Snapshot } from '../../../utils/schemas';

	export let data: PageData;
	const world: World | undefined = data?.world;
	const snapshots: Array<Snapshot> | undefined = data?.snapshots;

	let name = '';

	if (!world || !snapshots) {
		// Handle the case when data is not available
		console.warn('Data is not available.');
	}

	name = world?.name || '';

	function handleClick() {
		if (world) {
			openModal(Modal, {
				title: 'Delete World.',
				message: `This will delete world: ${world.name}, and make it unrecoverable.`,
				onConfirm: async () => {
					await fetch(`/api/worlds/${world.key}`, {
						method: 'DELETE'
					});

					goto(`/worlds`, { replaceState: true });

					closeModal();
				}
			});
		}
	}

	// Use the world and snapshots variables here
</script>

<svelte:head>
	<title>ChunkVault - World: {name}</title>
</svelte:head>
{#if world}
	<div class="flex w-full flex-col gap-4 p-4 md:p-0">
		<div class="breadcrumbs text-sm">
			<ul>
				<li><a href="/">Home</a></li>
				<li><a href="/worlds">Worlds</a></li>
				<li>{world.name}</li>
			</ul>
		</div>
		<div class="card card-side w-full bg-base-100">
			<div class="flex pl-6 md:items-start md:pt-7">
				<figure class="drop-shadow-neu">
					<img
						class="h-[82px] w-[82px] border-4 border-black drop-shadow-neu"
						src={world.image}
						alt={world.name}
					/>
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
						<p class="w-fit">Seed: {world.seed}</p>
						<div class="hidden md:divider md:divider-horizontal" />
						<p class="w-fit">Snapshots: {world.num_snapshots}</p>
					</div>
				</div>

				<div class="card-actions justify-center md:justify-end">
					<button class="btn-disabled btn-primary btn-sm btn">Edit</button>
					<button class="btn-disabled btn-secondary btn-sm btn">Share</button>
					<button on:click={handleClick} class=" btn-error btn-sm btn">Delete</button>
				</div>
			</div>
		</div>

		{#if snapshots}
			<WorldSnapshotList {snapshots} />
		{/if}
	</div>
{:else}
	<div>
		<h1>Error.</h1>
		<p>{error}</p>
	</div>
{/if}
