import requests


URL = "https://www.unisa.ac.za/sites/corporate/default/Apply-for-admission"


def fetch_page():
    """
    Fetch the UNISA admissions webpage.
    Returns the response object if successful.
    """

    response = requests.get(URL, timeout=30)
    response.raise_for_status()

    return response