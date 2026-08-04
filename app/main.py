"""
WatchTower AI
Main application entry point.
"""

from monitor import fetch_page
from parser import extract_text, contains_keyword
from notifier import send_email

KEYWORDS = [
  "Apply for admission",
]


def main():
    print("Connecting to UNISA...")

    response = fetch_page()

    print(f"Success! Status Code: {response.status_code}")

    text = extract_text(response.text)

    print("\nChecking for matching keywords...")

    found = contains_keyword(text, KEYWORDS)

    if found:
        print(f"✅ Keyword found: {found}")

        send_email(
            subject="🚨 WatchTower AI Alert",
            body=f"""
WatchTower AI has detected the keyword:

{found}

Visit the UNISA admissions page immediately:

https://www.unisa.ac.za/sites/corporate/default/Apply-for-admission
"""
        )

        print("📧 Email notification sent.")

    else:
        print("❌ No matching keywords found.")
        print("No email sent.")


if __name__ == "__main__":
    main()