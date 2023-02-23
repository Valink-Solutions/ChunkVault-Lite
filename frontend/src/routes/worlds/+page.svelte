<script lang="ts">
    import type { PageData } from '../../routes/$types';
	import WorldList from "../../components/WorldList.svelte";
    export let data: PageData;
</script>

<WorldList worlds={data.worlds}/>
