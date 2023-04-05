<script lang="ts">
	import WorldSnapshotList from '../../../components/WorldSnapshotList.svelte';
	import type { PageData } from './$types';
	import { formatBytes, formatDifficulty, shareWorld } from '../../../utils/reusables';
	import { openModal, closeModal } from 'svelte-modals';
	import Modal from '../../../components/Modal.svelte';
	import { goto } from '$app/navigation';
	import type { World, Snapshot } from '../../../utils/schemas';
	import { browser } from '$app/environment';
	import { toast } from '@zerodevx/svelte-toast';
	import EditModal from '../../../components/EditModal.svelte';

	export let data: PageData;
	let world: World = data.world;
	const snapshots: Array<Snapshot> = data.snapshots;

	let name = world.name;
	let is_public = world.is_public;

	function handleDelete() {
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

	function handleEdit() {
		openModal(EditModal, {
			title: world.name,
			world: world,
			onConfirm: async () => {
				const resp = await fetch(`/api/worlds/${world.key}`);
				world = await resp.json();

				goto(`/worlds/${world.key}`, { replaceState: true });

				closeModal();
			}
		});
	}

	async function handleShare() {
		let shareUrl = (await shareWorld(world)) || '';

		if (browser) {
			await navigator.clipboard.writeText(shareUrl);
		}

		if (!is_public) {
			is_public = !is_public;
		}

		toast.push(`Copied url for ${world.name}`);
	}

	// Use the world and snapshots variables here
</script>

<svelte:head>
	<title>ChunkVault - World: {name}</title>
</svelte:head>

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
				<div class="flex flex-1 flex-col md:flex-row">
					<h2 class="card-subtitle">
						Difficulty: {formatDifficulty(world.difficulty)}
					</h2>
					<div
						class="mx-2 hidden min-h-[1em] w-0.5 self-stretch bg-slate-400 opacity-100 dark:opacity-50 md:inline-block"
					/>
					<h2 class="card-subtitle">
						World Size: {formatBytes(world.size)}
					</h2>
				</div>
				<div class="flex w-fit flex-1 flex-col md:flex-row">
					<p class="w-fit">Seed: {world.seed}</p>
					<div
						class="mx-2 hidden min-h-[1em] w-0.5 self-stretch bg-slate-400 opacity-100 dark:opacity-50 md:inline-block"
					/>
					<p class="w-fit">Snapshots: {world.num_snapshots}</p>
				</div>
			</div>

			<div class="card-actions justify-center md:justify-end">
				<button on:click={handleEdit} class="btn-primary btn-sm btn">Edit</button>
				<button on:click={handleShare} class="btn-secondary btn-sm btn">Share</button>
				<button on:click={handleDelete} class=" btn-error btn-sm btn">Delete</button>
			</div>
		</div>
	</div>

	<WorldSnapshotList {snapshots} />
</div>
