<script lang="ts">
	import Icon from "@iconify/svelte";
    import { downloadSnapshot, formatBytes } from "../utils/reusables";
    import { openModal, closeModal } from 'svelte-modals'
    import Modal from './Modal.svelte'
    import { goto } from '$app/navigation';
	import type { Snapshot } from "../utils/schemas";

    function handleClick() {
        openModal(Modal, {
            title: "Delete Snapshot.",
            message: `This will delete snapshot: ${snapshot.name}, and make it unrecoverable.`,
            onConfirm: async () => {
                await fetch(`/api/snapshots/${snapshot.key}`, {
                    method: "DELETE"
                })

                goto(`/worlds`, { replaceState: true });

                closeModal();
            }
        })
    }


    export let snapshot: Snapshot;

    async function handeDownload() {
        await downloadSnapshot(snapshot.key, snapshot.parts, snapshot.name)
    }
</script>

<li class="card bg-base-100 p-6 flex flex-row justify-between w-full items-center">
    <div class="flex flex-row gap-3 items-center">
        <a href={`/worlds/${snapshot.world_id}`} class="btn btn-primary btn-sm">View World</a>
        <span class="badge badge-ghost text-xs min-w-fit">{formatBytes(snapshot.size)}</span>
        <h1 class="font-metropolis-italic">{snapshot.name}</h1>
    </div>
    <div class="flex flex-row gap-2 items-center">
        <button on:click={handeDownload} class="btn btn-ghost px-3 items-center gap-1">
            <span class="hidden md:block pt-0.5">Download</span>
            <Icon icon='mdi:cloud-download' class="text-lg"/>
        </button>
        <button on:click={handleClick} class="btn btn-error px-3 items-center gap-1">
            <span class="hidden md:block pt-0.5">Delete</span>
            <Icon icon='mdi:delete-forever' class="text-lg"/>
        </button>
    </div>
</li>