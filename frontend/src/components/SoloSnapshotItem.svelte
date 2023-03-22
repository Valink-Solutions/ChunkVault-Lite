<script lang="ts">
	import Icon from '@iconify/svelte';
	import { downloadSnapshot, formatBytes } from '../utils/reusables';
	import { openModal, closeModal } from 'svelte-modals';
	import Modal from './Modal.svelte';
	import { goto } from '$app/navigation';
	import type { Snapshot } from '../utils/schemas';

	function handleClick() {
		openModal(Modal, {
			title: 'Delete Snapshot.',
			message: `This will delete snapshot: ${snapshot.name}, and make it unrecoverable.`,
			onConfirm: async () => {
				await fetch(`/api/snapshots/${snapshot.key}`, {
					method: 'DELETE'
				});

				goto(`/worlds`, { replaceState: true });

				closeModal();
			}
		});
	}

	export let snapshot: Snapshot;

	async function handeDownload() {
		await downloadSnapshot(snapshot.key, snapshot.parts, snapshot.name);
	}
</script>

<li class="card flex w-full flex-row items-center justify-between bg-base-100 p-6">
	<div class="flex flex-row items-center gap-3">
		<a href={`/worlds/${snapshot.world_id}`} class="btn-primary btn-sm btn">View World</a>
		<span class="badge-ghost badge min-w-fit text-xs">{formatBytes(snapshot.size)}</span>
		<h1 class="font-metropolis-italic">{snapshot.name}</h1>
	</div>
	<div class="flex flex-row items-center gap-2">
		<button on:click={handeDownload} class="btn-ghost btn items-center gap-1 px-3">
			<span class="hidden pt-0.5 md:block">Download</span>
			<Icon icon="mdi:cloud-download" class="text-lg" />
		</button>
		<button on:click={handleClick} class="btn-error btn items-center gap-1 px-3">
			<span class="hidden pt-0.5 md:block">Delete</span>
			<Icon icon="mdi:delete-forever" class="text-lg" />
		</button>
	</div>
</li>
