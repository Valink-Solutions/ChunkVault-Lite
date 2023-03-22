<script lang="ts">
	import Icon from '@iconify/svelte';
	import { downloadSnapshot, formatBytes } from '../utils/reusables';
	import { openModal, closeModal } from 'svelte-modals';
	import Modal from './Modal.svelte';
	import { goto } from '$app/navigation';
	import type { Snapshot } from '../utils/schemas';

	export let snapshot: Snapshot;

	function handleClick() {
		openModal(Modal, {
			title: 'Delete Snapshot.',
			message: `This will delete snapshot: ${snapshot.name}, and make it unrecoverable.`,
			onConfirm: async () => {
				try {
					await fetch(`/api/snapshots/${snapshot.key}`, {
						method: 'DELETE'
					});
				} catch {
					return;
				}

				goto(`/worlds`, { replaceState: true });

				closeModal();
			}
		});
	}

	async function handeDownload() {
		await downloadSnapshot(snapshot.key, snapshot.parts, snapshot.name);
	}
</script>

<li class="card flex w-full flex-row items-center justify-between bg-base-100 p-6">
	<div class="flex flex-row items-center gap-3">
		<span class="badge-ghost badge min-w-fit text-xs">{formatBytes(snapshot.size)}</span>
		<h1 class="font-metropolis-italic">{snapshot.name}</h1>
	</div>
	<div class="flex flex-row items-center gap-2">
		<div
			class="tooltip tooltip-warning"
			data-tip="Warning: Downloading via the site, may be slow and error prone :("
		>
			<button on:click={handeDownload} class="btn-ghost btn items-center gap-1 px-3">
				<span class="hidden pt-0.5 md:block">Download</span>
				<Icon icon="mdi:cloud-download" class="text-lg" />
			</button>
		</div>
		<button on:click={handleClick} class="btn-error btn items-center gap-1 px-3">
			<span class="hidden pt-0.5 md:block">Delete</span>
			<Icon icon="mdi:delete-forever" class="text-lg" />
		</button>
	</div>
</li>
