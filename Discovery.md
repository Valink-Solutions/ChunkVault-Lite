---
title: "ChunkVault-Lite: Personal Minecraft Worlds Manager"
tagline: "Your own personal Minecraft worlds manager"
theme_color: "#f26daa"
git: "https://github.com/Valink-Solutions/ChunkVault-Lite"
homepage: "https://valink.io"
---

ChunkVault-Lite is a streamlined, all-inclusive world backup system specifically designed to work seamlessly with the Teller client. It empowers Minecraft enthusiasts to effortlessly upload, download, and share their world backups with friends or between devices.

Built with FastAPI as the backend and SvelteKit as the frontend, ChunkVault-Lite embraces a striking neubrutalism design that balances functionality with aesthetics.

**Please note:** ChunkVault-Lite is currently a proof of concept and has not been battle-tested. Use with caution and understand its limitations.

# Key Features & Use Cases

-   **World Storage:** Preserve your painstakingly crafted Minecraft builds and safeguard them from data loss.
-   **Easy Sharing:** Instantly share your creations with friends or the community at large.
-   **Device Transfer:** Effortlessly transfer your Minecraft world backups between devices, ensuring your work is always with you.

# Why Choose ChunkVault-Lite?

As a proof of concept, ChunkVault-Lite demonstrates the immense value of a user-friendly Minecraft backup system for the gaming community. Our mission is to showcase the potential of a platform that can overcome a myriad of limitations while remaining simple and effective.

You're welcome to use ChunkVault-Lite, but please be aware that it is not yet stable, and some features are still under development. We'll be adding core features as we progress, but we do not plan to expand beyond the basics, as another version is already in the works.

# Limitations & Considerations

Due to the constraints of Deta systems, ChunkVault-Lite currently only supports extremely small world files. We have implemented a resumable chunking system to bypass file size limitations in Deta's proxy/reverse proxy, but the Deta Micro/Drive size limit remains a challenge. Additionally, Deta Drive can only upload or replace files, not write to them directly.

So, go ahead and give ChunkVault-Lite a try, but remember to use it with caution and enjoy the simplicity of sharing and preserving your Minecraft world backups!