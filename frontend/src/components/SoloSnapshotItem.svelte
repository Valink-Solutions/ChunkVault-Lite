<script lang="ts">
	import Icon from '@iconify/svelte';
	import { downloadSnapshot, formatBytes } from '../utils/reusables';
	import { openModal, closeModal } from 'svelte-modals';
	import Modal from './Modal.svelte';
	import { goto } from '$app/navigation';
	import type { Snapshot } from '../utils/schemas';
	import moment from 'moment';

	function handleClick() {
		openModal(Modal, {
			title: 'Delete Snapshot.',
			message: `This will delete snapshot: ${snapshot.name}, and make it unrecoverable.`,
			onConfirm: async () => {
				await fetch(`/api/snapshots/${snapshot.key}`, {
					method: 'DELETE'
				});

				goto(`/snapshots`, { replaceState: true, invalidateAll: true });

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
		<a href={`/worlds/${snapshot.world_id}`} class="btn-primary btn items-center gap-1 px-3">
			<span class="hidden pt-0.5 md:block">View World</span>
			<Icon icon="mdi:eye" class="text-lg" />
		</a>
		<span class="badge-ghost badge min-w-fit text-xs">{formatBytes(snapshot.size)}</span>
		<div class="flex w-full flex-1 items-center">
			<h1 class="font-metropolis-italic">{snapshot.name}</h1>
			<div
				class="mx-2 hidden min-h-[1em] w-0.5 self-stretch bg-slate-400 opacity-100 dark:opacity-50 md:inline-block"
			/>
			<h1 class="hidden font-metropolis-italic text-sm lg:block">
				Created on {moment.unix(snapshot.created_at).format('MMM, DD YYYY [at] h:mmA')}
			</h1>
		</div>
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
