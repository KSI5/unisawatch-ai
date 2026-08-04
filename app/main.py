"""
UNISAWatch AI
Main application entry point.
"""

from monitor import fetch_page
from parser import extract_text, contains_keyword
from notifier import send_email
from state_manager import should_send_email, mark_email_sent

TARGET_YEAR = "2027"

KEYWORDS = [
    "undergraduate qualifications",
    "applications open",
    "apply now",
    "apply for admission",
]


def main():
    print("=" * 40)
    print("        UNISAWatch AI Started")
    print("=" * 40)

    print("\nConnecting to UNISA...")

    response = fetch_page()

    if response.status_code != 200:
        print(f"❌ Failed to connect. Status Code: {response.status_code}")
        return

    print(f"✅ Connected (Status Code: {response.status_code}")

    text = extract_text(response.text).lower()

    # Check target year
    if TARGET_YEAR.lower() not in text:
        print(f"❌ Target year '{TARGET_YEAR}' not found.")
        return

    print(f"✅ Target year '{TARGET_YEAR}' detected.")

    # Check supporting keywords
    found = contains_keyword(text, KEYWORDS)

    if not found:
        print("❌ No supporting keyword found.")
        return

    print(f"✅ Supporting keyword detected: '{found}'")

    # Check reminder interval
    if not should_send_email():
        print("📭 Reminder not due yet.")
        return

    # Send email
    send_email(
        subject=f"🚨 UNISAWatch AI Alert - {TARGET_YEAR} Applications Detected",
        body=f"""
Good news!

UNISAWatch AI detected that the UNISA admissions page appears to have been updated for {TARGET_YEAR}.

Supporting phrase detected:
{found}

Visit the admissions page:

https://www.unisa.ac.za/sites/corporate/default/Apply-for-admission

This is an automated reminder from UNISAWatch AI.
"""
    )

    mark_email_sent()

    print("📧 Email sent successfully.")


if __name__ == "__main__":
    main()