<script lang="ts">
    import type { PageData } from '../../routes/$types';
	import WorldList from "../../components/WorldList.svelte";
	import { formatBytes } from '../../utils/reusables';
    export let data: PageData;
</script>

<svelte:head>
  <title>ChunkVault - Worlds</title>
</svelte:head>

<div class="flex flex-col w-full gap-4 p-4 md:p-0">
    <div class="flex flex-row items-center justify-between w-full">
      <div class="text-sm breadcrumbs">
          <ul>
            <li><a href="/">Home</a></li> 
            <li>Worlds</li>
          </ul>
      </div>
      <div class="flex flex-row gap-2">
          <span><span class="font-metropolis-semibold">Total Snapshots:</span> {data.snapshots_info.count}</span>
          <span><span class="font-metropolis-semibold">Total Size:</span> {formatBytes(data.snapshots_info.total_size)}/<div class="tooltip tooltip-left" data-tip="This is based purely on Deta Space size, not how much actual room you have left"><button class="link">10 GB</button></div></span>
      </div>
    </div>
    
    <WorldList worlds={data.worlds}/>
</div>
