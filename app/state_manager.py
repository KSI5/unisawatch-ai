import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

STATUS_FILE = Path("status.json")


def load_status():
    if not STATUS_FILE.exists():
        return {"last_email_sent": None}

    with open(STATUS_FILE, "r") as f:
        return json.load(f)


def save_status(status):
    with open(STATUS_FILE, "w") as f:
        json.dump(status, f, indent=4)


def should_send_email():
    status = load_status()

    last = status.get("last_email_sent")

    if last is None:
        return True

    last_time = datetime.fromisoformat(last)
    now = datetime.now(timezone.utc)

    return now - last_time >= timedelta(days=2)


def mark_email_sent():
    status = load_status()

    status["last_email_sent"] = datetime.now(timezone.utc).isoformat()

    save_status(status)