import type { PageLoad } from './$types';
// import { env } from '$env/dynamic/public';
import type { Snapshot, World } from '../../utils/schemas';
export const prerender = false;

export const load = (async ({ fetch }) => {

    const res = await fetch(`/api-v1/snapshots/`);
    const json = await res.json();

    const snapshots: Array<Snapshot> = json.items;
    const count = json.count;
    const last = json.last;
    
    return {snapshots, count, last};
}) satisfies PageLoad;