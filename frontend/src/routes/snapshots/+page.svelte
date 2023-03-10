<svelte:head>
  <title>ChunkVault - Snapshots</title>
</svelte:head>

<script lang="ts">

    import SoloSnapshotItem from '../../components/SoloSnapshotItem.svelte';
import type { PageData } from '../../routes/$types';
	import { formatBytes } from '../../utils/reusables';
    export let data: PageData;
</script>

<div class="flex flex-col gap-4 w-full px-4 md:-0">
    <div class="flex flex-row items-center justify-between w-full">
        <div class="text-sm breadcrumbs">
            <ul>
                <li><a href="/">Home</a></li> 
                <li>Snapshots</li>
            </ul>
        </div>
        <div class="flex flex-row gap-2">
            <span><span class="font-metropolis-semibold">Total Snapshots:</span> {data.snapshots_info.num_snapshots}</span>
            <span><span class="font-metropolis-semibold">Total Size:</span> {formatBytes(data.snapshots_info.size)}/<div class="tooltip tooltip-left" data-tip="This is based purely on Deta Space size, not how much actual room you have left"><button class="link">10 GB</button></div></span>
        </div>
    </div>
    <ul class="flex flex-col gap-4 w-full">
        {#each data.snapshots as snapshot}
            <SoloSnapshotItem snapshot={snapshot} />
        {/each}
    </ul>
</div>