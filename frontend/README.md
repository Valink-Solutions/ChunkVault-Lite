# ChunkVault-Lite SvelteKit Frontend

## Theming

The theme for ChunkVault-Lite uses [DaisyUI](https://daisyui.com/)/[TailWindCSS](https://tailwindcss.com/) with custom classes for styling the site with a neubrutalism theme, which allows for simple visuals that are still appealing.

## Developing

Once you've cloned the project and installed dependencies with `pnpm install` (or `npm install` or `yarn`), start a development server:

```bash
pnpm dev

# or start the server and open the app in a new browser tab
pnpm dev -- --open
```

## Building

To create a production version of your app:

```bash
pnpm build
```

You can preview the production build with `pnpm preview`.

> The adapter used should always be the node adapter as it is needed for local and detas micros.

## Formatting

We use prettier and the tailwind prettier plugin to format the files in our project.

To format the files in the project:

```bash
pnpm format
```

**Remember to run Prettier regularly to keep your code clean and maintainable.**
