"""
WatchTower AI
Main application entry point.
"""

from monitor import fetch_page
from parser import extract_text, contains_keyword
from notifier import send_email
from state import notification_sent, mark_notification_sent

TARGET_YEAR = "2027"

KEYWORDS = [
    "undergraduate qualifications",
    "applications open",
    "apply now",
    "apply for admission",
]


def main():
    print("===================================")
    print("      WatchTower AI Started")
    print("===================================\n")

    print("Connecting to UNISA...")

    response = fetch_page()

    print(f"✅ Connected (Status Code: {response.status_code})")

    text = extract_text(response.text)

    if TARGET_YEAR.lower() not in text.lower():
        print(f"❌ {TARGET_YEAR} not found.")
        return

    found = contains_keyword(text, KEYWORDS)

    if not found:
        print("❌ Supporting keyword not found.")
        return

    if notification_sent():
        print("✅ Notification already sent.")
        return

    send_email(
        subject=f"🚨 UNISA {TARGET_YEAR} Applications Detected",
        body=f"""
Good news!

WatchTower AI detected that UNISA appears to have opened applications for {TARGET_YEAR}.

Supporting phrase:
{found}

Visit:
https://www.unisa.ac.za/sites/corporate/default/Apply-for-admission

Generated automatically by WatchTower AI.
"""
    )

    mark_notification_sent()

    print("📧 Email notification sent.")


if __name__ == "__main__":
    main()