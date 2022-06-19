from pathlib import Path
from datetime import datetime, timedelta


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def get_datetime_n_days_ago(num_days_ago: int) -> str:
    today = datetime.now()
    d = timedelta(days=num_days_ago)
    target_dt = today - d
    return target_dt.strftime("%d/%m/%Y")
