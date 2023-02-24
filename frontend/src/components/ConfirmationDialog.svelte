<script lang="ts">

    let is_open: boolean = false;

    function modifyDialog() {
        is_open = !is_open;
    }
</script>

<button class="btn btn-ghost" on:click={modifyDialog}>
    Open Dialog
</button>

<div style={is_open ? "display: none;" : ""}>
    <div class="absolute top-0 left-0 bg-black w-screen h-screen opacity-30 overflow-hidden">
    </div>
    
    <div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 card bg-base-100 min-w-[400px]">
        <div class="card-body">
            <h1 class="card-title">Confirm</h1>
            <p>please confirm you want to suck deeze nuts.</p>
            <div class="card-actions justify-end">
                <button class="btn btn-primary">Confirm</button>
                <button class="btn btn-error" on:click={modifyDialog}>Close</button>
            </div>
        </div>
    </div>
</div>