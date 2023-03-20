<script lang="ts">
    import { closeModal } from 'svelte-modals'
  
     export let isOpen: Boolean

     export let title: String

     export let message: String

     export let onConfirm
  
</script>
  
{#if isOpen}
<div role="dialog" class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 card bg-base-100 z-30 min-w-[400px]">
    <div class="card-body">
        <h2 class="card-title">{title}</h2>
        <p>{message}</p>
        <div class="card-actions justify-between md:justify-end">
            <button on:click={closeModal} class="btn btn-ghost">Close</button>
            <button on:click={onConfirm} class="btn btn-primary">Confirm</button>
        </div>
    </div>
</div>
{/if}
  
<style>
    /* .modal {
        position: absolute;
        top: 0;
        bottom: 0;
        right: 0;
        left: 0;
        z-index: 30;
        pointer-events: none;
    } */
</style>