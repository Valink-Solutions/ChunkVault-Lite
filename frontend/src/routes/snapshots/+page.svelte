<script lang="ts">
	import SoloSnapshotItem from '../../components/SoloSnapshotItem.svelte';
	import { formatBytes } from '../../utils/reusables';
	import type { Snapshot } from '../../utils/schemas';
	import { infoStore, snapshotStore } from '../../utils/snapshotStore';

	let snapshots: Array<Snapshot>;

	let info: {
		num_snapshots: number;
		size: number;
	};

	snapshotStore.subscribe((value) => {
		snapshots = value.snapshots;
	});

	infoStore.subscribe((value) => {
		info = value;
	});
</script>

<svelte:head>
	<title>ChunkVault - Snapshots</title>
</svelte:head>

<div class="md:-0 flex w-full flex-col gap-4 px-4">
	<div class="flex w-full flex-row items-center justify-between">
		<div class="breadcrumbs hidden text-sm md:block">
			<ul>
				<li><a href="/">Home</a></li>
				<li>Snapshots</li>
			</ul>
		</div>
		<div class="flex flex-row gap-2">
			<span
				><span class="font-metropolis-semibold">Total Snapshots:</span>
				{info.num_snapshots}</span
			>
			<span
				><span class="font-metropolis-semibold">Total Size:</span>
				{formatBytes(info.size)}/
				<div
					class="tooltip tooltip-left"
					data-tip="This is based purely on Deta Space size, not how much actual room you have left"
				>
					<button class="link">10 GB</button>
				</div></span
			>
		</div>
	</div>
	<ul class="flex w-full flex-col gap-4">
		{#each snapshots as snapshot}
			<SoloSnapshotItem {snapshot} />
		{/each}
	</ul>
</div>
