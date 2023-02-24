<script lang="ts">
    import WorldSnapshotList from '../../../components/WorldSnapshotList.svelte';
    import type { PageData } from '../../../routes/$types';
	import { formatBytes } from '../../../utils/reusables';
	import type { Snapshot } from '../../../utils/schemas';
    export let data: PageData;
    const world = data.world;

    let snapshots_size: number = 0;

    function getSnapshotSizes(snapshots: Array<Snapshot>) {
        snapshots.forEach(snapshot => {
            snapshots_size += snapshot?.size || 0;
        });
    }

    getSnapshotSizes(world.snapshots)
    
</script>

<svelte:head>
  <title>ChunkVault - World: {world.name}</title>
</svelte:head>

<div class="flex flex-col gap-4 w-full p-4 md:p-0">
    <div class="text-sm breadcrumbs">
        <ul>
          <li><a href="/">Home</a></li> 
          <li><a href="/worlds">Worlds</a></li> 
          <li>{world.name}</li>
        </ul>
    </div>
    <div class="card card-side w-full bg-base-100">
        <div class="flex md:items-start md:pt-7 pl-6">
            <figure class="drop-shadow-neo"><img class="border-4 border-black drop-shadow-neo h-[82px] w-[82px]" src={world.image} alt={world.name}/></figure>
        </div>
        <div class="card-body justify-center">
            <div class="flex flex-row justify-between items-center">
                <h1 class="card-title">{world.name}</h1>
                {#if (world.is_public)}
                    <span class="badge badge-sm badge-accent">Public</span>
                {:else}
                    <span class="badge badge-sm badge-ghost">Private</span>
                {/if}
            </div>
            <h2 class="card-subtitle">World Size: {formatBytes(world.size)}</h2>
            <p>Snapshots: {world.num_snapshots} | {formatBytes(snapshots_size)} in Total</p>
            <div class="card-actions justify-center md:justify-end">
                <button class="btn btn-primary btn-sm btn-disabled">Edit</button>
                <button class="btn btn-secondary btn-sm btn-disabled">Share</button>
                <button class="btn btn-error btn-sm btn-disabled">Delete</button>
            </div>
        </div>
    </div>
    
    <WorldSnapshotList snapshots={world.snapshots}/>
</div>