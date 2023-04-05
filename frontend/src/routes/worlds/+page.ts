import type { PageLoad } from './$types';
import { error } from '@sveltejs/kit';

// export const prerender = false;

export const load = (async ({ fetch }) => {
	try {
		const info_res = await fetch(`/api/snapshots/info/`);
		const info_json = await info_res.json();

		const info = {
			num_snapshots: info_json.num_snapshots,
			size: info_json.size
		};

		const res = await fetch(`/api/worlds`);
		const json = await res.json();

		const worlds = json.items;
		const last = json.last;
		const count = json.count;

		return {
			worlds,
			last,
			count,
			info
		};
	} catch (e) {
		console.error(e);

		throw error(500, 'An error occurred while loading the data.');
	}
}) satisfies PageLoad;
