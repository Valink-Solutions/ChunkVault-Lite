from deta import Deta

from application.utils.config import DETA_PROJECT_KEY

deta = Deta(DETA_PROJECT_KEY)

token_db = deta.Base("tokens")

log_db = deta.Base("logs")

upload_session_db = deta.Base("upload_sessions")

snapshot_db = deta.Base("snaphsots")

snapshot_drive = deta.Drive("snapshots")