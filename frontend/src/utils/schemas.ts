export interface World {
    key: string,
    name: string,
    image: string,
    num_snapshots: number,
    size: number
}

export interface WorldWithSnaps {
    key: string,
    name: string,
    image: string,
    num_snapshots: number,
    size: number
    snapshots: Array<Snapshot>
}

export interface Snapshot {
    key: string,
    world_id: string,
    name: string,
    size: number
    created_at: number
}