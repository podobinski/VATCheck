import requests
import datetime

def check_vat_nip(nip):
    """
    Retrieves information about a single subject using their NIP
    """
    url = f"https://wl-api.mf.gov.pl/api/search/nip/{nip}?date={datetime.date.today()}"
    headers = {"User-Agent": "Mozilla/5.0"} # add a user agent header to avoid 403 Forbidden error
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()["result"]["subject"]
    elif response.status_code == 400:
        raise Exception("Niepoprawny parametr na wejściu")
    else:
        raise Exception("Nieznany błąd")
