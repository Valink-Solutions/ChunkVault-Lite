export interface World {
    key: String,
    name: String,
    image: String,
    num_snapshots: Number,
    size: Number
}

export interface WorldWithSnaps {
    key: String,
    name: String,
    image: String,
    num_snapshots: Number,
    size: Number
    snapshots: Array<Snapshot>
}

export interface Snapshot {
    key: String,
    world_id: String,
    name: String,
    size: Number
    created_at: Number
}