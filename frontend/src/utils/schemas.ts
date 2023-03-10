export interface World {
    key: string
    name: string
    image: string
    difficulty: number
    seed: string
    num_snapshots: number
    size: number
    is_public: boolean
}

export interface WorldWithSnaps {
    key: string
    name: string
    image: string
    difficulty: number
    seed: string
    num_snapshots: number
    size: number
    is_public: boolean
    snapshots: Array<Snapshot>
}

export interface Snapshot {
    key: string
    world_id: string
    name: string
    parts: number
    size: number
    created_at: number
}