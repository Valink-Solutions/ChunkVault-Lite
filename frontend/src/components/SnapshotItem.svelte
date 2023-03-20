<script lang="ts">
	import Icon from "@iconify/svelte";
    import { downloadSnapshot, formatBytes } from "../utils/reusables";
    import { openModal, closeModal } from 'svelte-modals'
    import Modal from './Modal.svelte'
    import { goto } from '$app/navigation';
	import type { Snapshot } from "../utils/schemas";

    export let snapshot: Snapshot;

    function handleClick() {
        openModal(Modal, {
            title: "Delete Snapshot.",
            message: `This will delete snapshot: ${snapshot.name}, and make it unrecoverable.`,
            onConfirm: async () => {
                try {
                    await fetch(`/api/snapshots/${snapshot.key}`, {
                        method: "DELETE"
                    })
                } catch {
                    return;
                }

                goto(`/worlds`, { replaceState: true });

                closeModal();
            }
        })
    }

    async function handeDownload() {
        await downloadSnapshot(snapshot.key, snapshot.parts, snapshot.name)
    }

</script>

<li class="card bg-base-100 p-6 flex flex-row justify-between w-full items-center">
    <div class="flex flex-row gap-3 items-center">
        <span class="badge badge-ghost text-xs min-w-fit">{formatBytes(snapshot.size)}</span>
        <h1 class="font-metropolis-italic">{snapshot.name}</h1>
    </div>
    <div class="flex flex-row gap-2 items-center">
        <div class="tooltip tooltip-warning" data-tip="Warning: Downloading via the site, may be slow and error prone :(">
            <button on:click={handeDownload} class="btn btn-ghost px-3 items-center gap-1">
                <span class="hidden md:block pt-0.5">Download</span>
                <Icon icon='mdi:cloud-download' class="text-lg"/>
            </button>
        </div>
        <button on:click={handleClick} class="btn btn-error px-3 items-center gap-1">
            <span class="hidden md:block pt-0.5">Delete</span>
            <Icon icon='mdi:delete-forever' class="text-lg"/>
        </button>
    </div>
</li>