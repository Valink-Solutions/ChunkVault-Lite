import type { PageLoad } from './$types';
// import { env } from '$env/dynamic/public';
import type { World } from '../../utils/schemas';

export const load = (async ({ fetch }) => {

    const res = await fetch(`/api-v1/worlds/`);
    const json = await res.json();

    const worlds: Array<World> = json.items;
    const count = json.count;
    const last = json.last;
    
    return {worlds, count, last};
}) satisfies PageLoad;