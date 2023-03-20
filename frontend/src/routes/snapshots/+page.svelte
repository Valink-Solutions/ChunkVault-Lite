<script lang="ts">

    import SoloSnapshotItem from '../../components/SoloSnapshotItem.svelte';
    import type { PageData } from '../../routes/$types';
	import { formatBytes } from '../../utils/reusables';
    export let data: PageData;
    const snapshots = data?.snapshots;
    const snapshots_info = data?.snapshots_info;

    if (!snapshots || !snapshots_info) {
        // Handle the case when data is not available
        console.warn('Data is not available.');
    }

</script>

<svelte:head>
  <title>ChunkVault - Snapshots</title>
</svelte:head>

<div class="flex flex-col gap-4 w-full px-4 md:-0">
    <div class="flex flex-row items-center justify-between w-full">
        <div class="text-sm breadcrumbs">
            <ul>
                <li><a href="/">Home</a></li> 
                <li>Snapshots</li>
            </ul>
        </div>
        <div class="flex flex-row gap-2">
            <span><span class="font-metropolis-semibold">Total Snapshots:</span> {snapshots_info.num_snapshots}</span>
            <span><span class="font-metropolis-semibold">Total Size:</span> {formatBytes(snapshots_info.size)}/<div class="tooltip tooltip-left" data-tip="This is based purely on Deta Space size, not how much actual room you have left"><button class="link">10 GB</button></div></span>
        </div>
    </div>
    <ul class="flex flex-col gap-4 w-full">
        {#each snapshots as snapshot}
            <SoloSnapshotItem snapshot={snapshot} />
        {/each}
    </ul>
</div>