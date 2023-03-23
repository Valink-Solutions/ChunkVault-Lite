import { writable } from 'svelte/store';
import type { World } from '../utils/schemas';

interface WorldStore {
	worlds: Array<World>;
	last: string;
	count: number;
}

const initialData: WorldStore = {
	worlds: [],
	last: '',
	count: 0
};

export const worldStore = writable<WorldStore>(initialData);
