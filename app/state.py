from pathlib import Path

STATE_FILE = Path("state.txt")


def notification_sent():
    """
    Returns True if a notification has already been sent.
    """
    return STATE_FILE.exists()


def mark_notification_sent():
    """
    Marks that a notification has been sent.
    """
    STATE_FILE.write_text("sent")


def reset_notification():
    """
    Clears the notification state.
    """
    if STATE_FILE.exists():
        STATE_FILE.unlink()