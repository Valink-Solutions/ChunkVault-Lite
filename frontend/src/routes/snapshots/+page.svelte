<svelte:head>
  <title>ChunkVault - Snapshots</title>
</svelte:head>

<script lang="ts">

    import SoloSnapshotItem from '../../components/SoloSnapshotItem.svelte';
import type { PageData } from '../../routes/$types';
    export let data: PageData;
    const snapshots = data.snapshots;
</script>

<ul class="flex flex-col gap-4 w-full">
    {#each snapshots as snapshot}
        <SoloSnapshotItem snapshot={snapshot} />
    {/each}
</ul>