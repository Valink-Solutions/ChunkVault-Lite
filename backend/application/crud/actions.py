from application.utils.connections import deleted_snapshots_db, snapshot_drive


def delete_snapshots():
    data = deleted_snapshots_db.fetch()

    for item in data.items:
        for part in range(item["parts"] if item["parts"] > 0 else 50):
            try:
                snapshot_drive.delete(
                    f"{item['snapshot_id']}/{item['name']}.part{part+1}"
                )
            except Exception:
                pass

        deleted_snapshots_db.delete(item["key"])
