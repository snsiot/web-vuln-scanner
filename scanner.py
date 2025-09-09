import requests
from bs4 import BeautifulSoup

# Payloads to test vulnerabilities
xss_payload = "<script>alert(1)</script>"
sqli_payload = "' OR '1'='1"

def scan_url(url):
    print(f"Scanning {url}...")

    try:
        response = requests.get(url)
        content = response.text
        soup = BeautifulSoup(content, "html.parser")

        # Find all forms on the page
        forms = soup.find_all("form")
        print(f"Found {len(forms)} form(s).")

        # Check if the XSS payload appears in the response
        if xss_payload in content:
            print("[!] Potential XSS vulnerability found.")

        # (You can expand this scanner further)
    except Exception as e:
        print(f"Error scanning {url}: {e}")

if __name__ == "__main__":
    target_url = input("Enter the URL to scan: ")
    scan_url(target_url)
