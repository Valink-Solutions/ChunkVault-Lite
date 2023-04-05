import type { PageLoad } from './$types';
// import { env } from '$env/dynamic/public';
import type { World, Snapshot } from '../../../utils/schemas';
import { error } from '@sveltejs/kit';
export const prerender = false;

export const load = (async ({ params, fetch }) => {
	try {
		const world_id = params.id;

		const res = await fetch(`/api/worlds/${world_id}`);
		const world: World = await res.json();

		const snap_res = await fetch(`/api/worlds/${world_id}/snapshots`);
		const data = await snap_res.json();
		const snapshots: Array<Snapshot> = data.items;

		return {
			world: world,
			snapshots: snapshots
		};
	} catch (e) {
		console.error(e);

		throw error(500, 'An error occurred while loading the data.');
	}
}) satisfies PageLoad;
