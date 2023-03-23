import { worldStore } from '../../utils/worldStore';
import type { PageLoad } from './$types';
import { infoStore } from '../../utils/snapshotStore';

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

		worldStore.set({
			worlds,
			last,
			count
		});

		infoStore.set(info);

		return {};
	} catch (error) {
		console.error(error);
		return {
			error: 'An error occurred while loading the data.'
		};
	}
}) satisfies PageLoad;
