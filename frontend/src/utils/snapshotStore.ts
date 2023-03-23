import { writable } from 'svelte/store';
import type { Snapshot } from '../utils/schemas';

interface InfoStore {
	num_snapshots: number;
	size: number;
}

interface SnapshotStore {
	snapshots: Array<Snapshot>;
	last: string;
	count: number;
}

const initialSnapshotData: SnapshotStore = {
	snapshots: [],
	last: '',
	count: 0
};

const initialInfoData: InfoStore = {
	num_snapshots: 0,
	size: 0
};

export const snapshotStore = writable<SnapshotStore>(initialSnapshotData);

export const infoStore = writable<InfoStore>(initialInfoData);
