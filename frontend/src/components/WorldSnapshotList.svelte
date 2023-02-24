<script lang="ts">
	import type { Snapshot } from "../utils/schemas";
	import SnapshotItem from "./SnapshotItem.svelte";

    export let snapshots: Array<Snapshot>;
</script>
<ul class="flex flex-col gap-4 w-full">
    {#each snapshots as snapshot}
        <SnapshotItem snapshot={snapshot} /> 
    {/each}
</ul>