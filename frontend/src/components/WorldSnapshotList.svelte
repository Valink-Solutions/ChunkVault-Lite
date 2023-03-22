<script lang="ts">
	import type { Snapshot } from '../utils/schemas';
	import SnapshotItem from './SnapshotItem.svelte';

	export let snapshots: Array<Snapshot>;
</script>

<ul class="flex w-full flex-col gap-4">
	{#each snapshots as snapshot}
		<SnapshotItem {snapshot} />
	{/each}
</ul>
