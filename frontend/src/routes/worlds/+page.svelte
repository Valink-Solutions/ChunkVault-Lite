<script lang="ts">
    import type { PageData } from '../../routes/$types';
	import WorldList from "../../components/WorldList.svelte";
    export let data: PageData;
</script>

<svelte:head>
  <title>ChunkVault - Worlds</title>
</svelte:head>

<div class="flex flex-col w-full gap-4 p-4 md:p-0">
    <div class="text-sm breadcrumbs">
        <ul>
          <li><a href="/">Home</a></li> 
          <li>Worlds</li>
        </ul>
    </div>
    
    <WorldList worlds={data.worlds}/>
</div>
