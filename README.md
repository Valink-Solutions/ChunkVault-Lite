![ChunkVault-Lite Logo](/extras/images/chunkvailt-lite-logo.png)

# ChunkVault-Lite

ChunkVault-Lite is an all in one world backup system meant to work with the teller client, allowing users to upload, download and share minecraft world backups.

## Design System

We use DaisyUI with a Neubrutalism styling.

## Limitations

only extremely small world files are allowed because of the limitations of detas systems, we use a resumable chunking system to bypass any file size limitations in detas proxy/reverseproxy but we cannot bypass detas micros size limit, and the fact we can only upload or replace files and not write to files in the drives.