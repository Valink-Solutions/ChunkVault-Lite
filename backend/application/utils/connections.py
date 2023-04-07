from application.utils.config import DETA_PROJECT_KEY
from deta import Deta

deta = Deta(project_key=DETA_PROJECT_KEY)

upload_session_db = deta.Base("upload_sessions")

worlds_db = deta.Base("worlds")

snapshot_db = deta.Base("snapshots")

snapshot_drive = deta.Drive("snapshots")

deleted_snapshots_db = deta.Base("deleted_snapshots")
