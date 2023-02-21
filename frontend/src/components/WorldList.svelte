<script lang="ts">
	import WorldListItem from "../components/WorldListItem.svelte";
	import type { World } from "../utils/schemas";
    
    export let worlds: Array<World>;
</script>

<ul class="flex flex-col gap-5 px-4 md:px-0">
    {#each worlds as world}
        <li>
            <WorldListItem world={world} />
        </li>
    {/each}
</ul>
