<script lang="ts">
	import type { PageData } from './$types';
	import WorldList from '../../components/WorldList.svelte';
	import { formatBytes } from '../../utils/reusables';
	import type { World } from '../../utils/schemas';
	export let data: PageData;
	const worlds: Array<World> = data.worlds;
	const info = data.info;
</script>

<svelte:head>
	<title>ChunkVault - Worlds</title>
</svelte:head>

<div class="flex w-full flex-grow flex-col gap-4 p-4 md:p-0">
	<div class="flex w-full flex-row items-center justify-between">
		<div class="breadcrumbs hidden text-sm md:block">
			<ul>
				<li><a href="/">Home</a></li>
				<li>Worlds</li>
			</ul>
		</div>
		<div class="flex flex-row gap-2">
			<span
				><span class="font-metropolis-semibold">Total Snapshots:</span>
				{info.num_snapshots}</span
			>
			<span>
				<span class="font-metropolis-semibold"> Total Size: </span>
				{formatBytes(info.size)}
				/
				<div
					class="tooltip tooltip-left"
					data-tip="This is based purely on Deta Space size, not how much actual room you have left"
				>
					<button class="link"> 10 GB </button>
				</div>
			</span>
		</div>
	</div>
	<WorldList {worlds} />
</div>
