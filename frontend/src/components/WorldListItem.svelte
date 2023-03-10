<script lang="ts">
	import { formatBytes, formatDifficulty } from "../utils/reusables";
	import type { World } from "../utils/schemas";
    export let world: World;

</script>

<div class="card card-side w-full bg-base-100">
    <div class="flex md:items-start md:pt-7 pl-6">
        <figure class="drop-shadow-neo"><img class="border-4 border-black h-[82px] w-[82px]" src={world.image} alt={world.name}/></figure>
    </div>
    <div class="card-body justify-center">
        <div class="flex flex-row justify-between items-center">
            <h1 class="card-title">{world.name}</h1>
            {#if (world.is_public)}
                <span class="badge badge-sm badge-accent">Public</span>
            {:else}
                <span class="badge badge-sm badge-ghost">Private</span>
            {/if}
        </div>
        <h2 class="card-subtitle">Difficulty: {formatDifficulty(world.difficulty)} | World Size: {formatBytes(world.size)}</h2>
        <p>Snapshots: {world.num_snapshots}</p>
        <div class="card-actions justify-center md:justify-end">
            <a href={`/worlds/${world.key}`} class="btn btn-primary btn-sm">View</a>
            <a href="/" class="btn btn-secondary btn-sm btn-disabled">Share</a>
            <a href="/" class="btn btn-error btn-sm btn-disabled">Delete</a>
        </div>
    </div>
</div>