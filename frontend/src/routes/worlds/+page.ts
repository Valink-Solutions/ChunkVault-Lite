import type { PageLoad } from './$types';
// import { env } from '$env/dynamic/public';
import type { World } from '../../utils/schemas';
export const prerender = false;

export const load = (async ({ fetch }) => {

    const size_res = await fetch(`/api-v1/snapshots/info/`);
    const snapshots_info = await size_res.json()

    const res = await fetch(`/api-v1/worlds/`);
    const json = await res.json();

    const worlds: Array<World> = json.items;
    const count = json.count;
    const last = json.last;
    
    return {worlds, snapshots_info, count, last};
}) satisfies PageLoad;