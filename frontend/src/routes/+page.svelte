<script>
	import Icon from '@iconify/svelte';
</script>

<svelte:head>
	<title>ChunkVault - Home</title>
</svelte:head>

<div class="flex w-full flex-col items-center justify-center gap-4 px-4 md:p-0">
	<a href="/worlds" class="btn-primary btn-lg btn w-full items-center gap-1">
		<Icon icon="mdi:earth-box" class="text-2xl" />
		<span class="pt-0.5">Worlds</span>
	</a>
	<a href="/snapshots" class="btn-secondary btn-lg btn w-full items-center gap-1">
		<Icon icon="mdi:file-cabinet" class="text-2xl" />
		<span class="pt-0.5">Snapshots</span>
	</a>
</div>
