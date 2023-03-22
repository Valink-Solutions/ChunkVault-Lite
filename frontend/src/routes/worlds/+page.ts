import type { PageLoad } from './$types';
// import { env } from '$env/dynamic/public';
import type { World } from '../../utils/schemas';
export const prerender = false;

export const load = (async ({ fetch }) => {
	try {
		const size_res = await fetch(`/api/snapshots/info/`);
		const snapshots_info = await size_res.json();

		const res = await fetch(`/api/worlds`);
		const json = await res.json();

		const worlds: Array<World> = json.items;
		const count = json.count;
		const last = json.last;

		return {
			worlds: worlds,
			snapshots_info: snapshots_info,
			count: count,
			last: last
		};
	} catch (error) {
		console.error(error);
		return {
			error: 'An error occurred while loading the data.'
		};
	}
}) satisfies PageLoad;
