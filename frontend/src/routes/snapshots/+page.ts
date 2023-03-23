import type { PageLoad } from './$types';
import { infoStore, snapshotStore } from '../../utils/snapshotStore';

// export const prerender = false;

export const load = (async ({ fetch }) => {
	try {
		const info_res = await fetch(`/api/snapshots/info/`);
		const info_json = await info_res.json();

		const info = {
			num_snapshots: info_json.num_snapshots,
			size: info_json.size
		};

		const res = await fetch(`/api/snapshots`);
		const json = await res.json();

		const snapshots = json.items;
		const last = json.last;
		const count = json.count;

		snapshotStore.set({
			snapshots,
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
