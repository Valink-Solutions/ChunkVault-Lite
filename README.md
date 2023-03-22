![ChunkVault-Lite Logo](/extras/images/chunkvailt-lite-logo.png)

# ChunkVault-Lite

## Overview

ChunkVault Lite is a personal Minecraft world backup service designed to provide users with a seamless and efficient way to create versioned snapshots of their Minecraft worlds. This ensures secure storage, easy browsing, and the ability to share worlds with friends. The application is hosted on Deta Space, a personal cloud hosting service tailored for small applications. The frontend of ChunkVault Lite is built using SvelteKit and DaisyUI with a custom neubrutalism theme, while the backend leverages FastAPI.

## Key Features

Host your own instance on Deta Space
Create versioned snapshots of Minecraft worlds
Secure storage and easy browsing
Share worlds with friends
Teller-CLI tool for uploading, downloading, and sharing via the command line

## Technologies Used

- Frontend: SvelteKit, DaisyUI, Neubrutalism design
- Backend: FastAPI
- Hosting: Deta Space
- CLI: Teller-CLI tool for command-line interaction

## Technical Challenges

Due to Deta's resource constraints, such as a 250 MB RAM limit and a 10-second time to live, several technical challenges had to be overcome:

- Broken FastAPI background tasks: Deta's limitations caused FastAPI background tasks to break. To resolve this, files had to be uploaded pre-chunked by the user. This led to the creation of the teller-cli tool to interact with the backend alongside the frontend, enabling command-line-based uploading, downloading, and sharing.

- Chunked download feature: The 250 MB RAM limit necessitated storing files in a chunked format on the backend. To facilitate downloading from the frontend, a chunked download feature was implemented. However, this resulted in slow browser-based downloads.

- Unique world identification: To uniquely identify worlds, they were given IDs in the format `f'{world_seed}-{world_name}'.` This was necessary as there is no proper way to store an ID in a Minecraft world, based on the testing conducted.

## Future Plans

ChunkVault Lite serves as a foundation for the development of a more robust version, known simply as ChunkVault. This version will be built using Rust and will incorporate erasure coding and most object storage best practices. It will also be open source, allowing for community contributions and enhancements.

## Getting Started

To begin development on ChunkVault-Lite, you must first link a project from your Deta Space account. While the backend can function locally without any code modifications, the frontend necessitates adjustments to the API calls. Specifically, you need to replace `/api` with `http://localhost:8080` in every fetch call. This ensures that the calls are routed locally, rather than attempting to operate through Deta's proxy or reverse proxy.

For comprehensive information on backend development, please refer to the backend [README](/backend/README.md). Likewise, for guidance on frontend development, consult the frontend [README](/frontend/README.md).