<script lang="ts">
    import type { PageData } from './$types';
	import WorldList from "../components/WorldList.svelte";
    export let data: PageData;
</script>

<WorldList worlds={data.worlds}/>
