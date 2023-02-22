<script lang="ts">
	import type { World } from "../utils/schemas";

    export let world: World;

    function formatBytes(bytes: number) {

        if (bytes < 1024) {
            return bytes + " bytes";
        } else if (bytes < 1048576) {
            return (bytes / 1024).toFixed(2) + " KB";
        } else if (bytes < 1073741824) {
            return (bytes / 1048576).toFixed(2) + " MB";
        } else {
            return (bytes / 1073741824).toFixed(2) + " GB";
        }
    }
</script>

<div class="card card-side w-full bg-base-100">
    <figure><img class="h-full min-w-[164px]" src="/icon.png" alt="Movie"/></figure>
    <div class="card-body justify-center">
        <div class="flex flex-row justify-between items-center">
            <h1 class="card-title">{world.name}</h1>
            <span class="badge badge-sm badge-ghost">Public</span>
        </div>
        <h2 class="card-subtitle">World Size: {formatBytes(world.size)}</h2>
        <p>Snapshots: {world.num_snapshots}</p>
        <div class="card-actions justify-center md:justify-end">
            <button class="btn btn-primary btn-sm">Edit</button>
            <button class="btn btn-secondary btn-sm">Share</button>
            <button class="btn btn-error btn-sm">Delete</button>
        </div>
    </div>
</div>