<script lang="ts">
	import Icon from '@iconify/svelte';
	import {
		downloadPublicSnapshot,
		formatBytes,
		formatDifficulty
	} from '../../../../utils/reusables';
	import type { PublicWorld } from '../../../../utils/schemas';
	import type { PageData } from './$types';
	import moment from 'moment';

	export let data: PageData;
	const world: PublicWorld = data.world;

	let name = world.name;

	async function handeDownload() {
		if (world) {
			await downloadPublicSnapshot(world.key, world.parts, world.name);
		}
	}
</script>

<svelte:head>
	<title>ChunkVault - World: {name}</title>
</svelte:head>

<div class="flex w-full flex-col gap-4 p-4 md:p-0">
	<div class="card card-side w-full bg-base-100">
		<div class="flex pl-6 md:items-start md:pt-7">
			<figure class="drop-shadow-neu">
				<img
					class="h-[82px] w-[82px] border-4 border-black drop-shadow-neu"
					src={world.image}
					alt={world.name}
				/>
			</figure>
		</div>
		<div class="card-body justify-center">
			<div class="flex flex-row gap-2 md:gap-4">
				<div class="flex h-full w-full flex-col">
					<div class="flex flex-row items-center justify-between">
						<h1 class="card-title">{world.name}</h1>
					</div>

					<div>
						<div class="flex flex-col md:flex-row">
							<h2 class="card-subtitle">
								Difficulty: {formatDifficulty(world.difficulty)}
							</h2>
							<div class="hidden md:divider md:divider-horizontal" />
							<h2 class="card-subtitle">
								World Size: {formatBytes(world.full_size)}
							</h2>
							<div class="hidden md:divider md:divider-horizontal" />
							<h2 class="card-subtitle">
								Last snapped: {moment.unix(world.created_at).format('MMM, DD YYYY [at] h:mmA')}
							</h2>
						</div>
						<div class="flex w-fit flex-col md:flex-row">
							<p class="w-fit">Seed: {world.seed}</p>
						</div>
					</div>
				</div>

				<div class="flex h-full w-fit items-center justify-end">
					<button on:click={handeDownload} class="btn-ghost btn items-center gap-1 px-3">
						<span class="hidden pt-0.5 md:block">Download</span>
						<Icon icon="mdi:cloud-download" class="text-lg" />
					</button>
				</div>
			</div>
		</div>
	</div>
</div>
