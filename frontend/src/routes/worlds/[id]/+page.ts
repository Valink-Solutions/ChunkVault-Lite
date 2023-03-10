import type { PageLoad } from './$types';
// import { env } from '$env/dynamic/public';
import type { WorldWithSnaps } from '../../../utils/schemas';
export const prerender = false;

export const load = (async ({ params, fetch }) => {

    const world_id = params.id

    const res = await fetch(`/api/worlds/${world_id}`);
    const world: WorldWithSnaps = await res.json();
    
    return {
        world: world
    };
}) satisfies PageLoad;