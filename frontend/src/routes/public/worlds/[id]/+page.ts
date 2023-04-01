import type { PublicWorld } from '../../../../utils/schemas';
import type { PageLoad } from './$types';
// import { env } from '$env/dynamic/public';
export const prerender = false;

export const load = (async ({ params, fetch }) => {
	try {
		const world_id = params.id;

		const res = await fetch(`/api/public/worlds/${world_id}`);
		const world: PublicWorld = await res.json();

		return {
			world: world
		};
	} catch (error) {
		console.error(error);
		return {
			error: 'An error occurred while loading the data.'
		};
	}
}) satisfies PageLoad;
