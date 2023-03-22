<script lang="ts">
	import WorldListItem from '../components/WorldListItem.svelte';
	import type { World } from '../utils/schemas';

	export let worlds: Array<World>;
</script>

<ul class="flex flex-col gap-5">
	{#each worlds as world}
		<li>
			<WorldListItem {world} />
		</li>
	{/each}
</ul>
