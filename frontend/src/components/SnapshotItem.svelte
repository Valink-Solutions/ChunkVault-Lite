<script lang="ts">
	import Icon from "@iconify/svelte";
    import { formatBytes } from "../utils/reusables";
	import type { Snapshot } from "../utils/schemas";


    export let snapshot: Snapshot;

</script>

<li class="card bg-base-100 p-6 flex flex-row justify-between w-full items-center">
    <div class="flex flex-row gap-3 items-center">
        <span class="badge badge-ghost text-xs min-w-fit">{formatBytes(snapshot.size)}</span>
        <h1 class="font-metropolis-italic">{snapshot.name}</h1>
    </div>
    <div class="flex flex-row gap-2 items-center">
        <a href={`/api-v1/snapshots/${snapshot.key}?download=true`} class="btn btn-ghost px-3 items-center gap-1" download>
            <span class="hidden md:block pt-0.5">Download</span>
            <Icon icon='mdi:cloud-download' class="text-lg"/>
        </a>
        <button class="btn btn-error px-3 items-center gap-1 btn-disabled">
            <span class="hidden md:block pt-0.5">Delete</span>
            <Icon icon='mdi:delete-forever' class="text-lg"/>
        </button>
    </div>
</li>