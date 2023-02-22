---
title: "ChunkVault-Lite: Personal Minecraft Worlds Manager"
tagline: "Your own personal Minecraft worlds manager: private, secure & always online."
theme_color: "#f26daa"
git: "https://github.com/Valink-Solutions/ChunkVault-Lite"
homepage: "https://valink.io"
---


ChunkVault-Lite is an all in one world backup system meant to work with the teller client, allowing users to upload, download and share minecraft world backups.

## Limitations

only extremely small world files are allowed because of the limitations of detas systems, we use a resumable chunking system to bypass any file size limitations in detas proxy/reverseproxy but we cannot bypass detas micros size limit, and the fact we can only upload or replace files and not write to files in the drives.