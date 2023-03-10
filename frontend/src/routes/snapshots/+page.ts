import type { PageLoad } from './$types';
// import { env } from '$env/dynamic/public';
import type { Snapshot, World } from '../../utils/schemas';
export const prerender = false;

export const load = (async ({ fetch }) => {

    const size_res = await fetch(`/api/snapshots/info/`);
    const snapshots_info = await size_res.json()

    const res = await fetch(`/api/snapshots`);
    const json = await res.json();

    const snapshots: Array<Snapshot> = json.items;
    const count = json.count;
    const last = json.last;
    
    return {
        snapshots: snapshots,
        snapshots_info: snapshots_info,
        count: count,
        last: last
    };
}) satisfies PageLoad;