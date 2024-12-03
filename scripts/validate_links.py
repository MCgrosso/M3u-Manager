import requests

def validate_m3u(urls):
    valid_urls = []
    for url in urls:
        try:
            response = requests.head(url, timeout=5)
            if response.status_code == 200:
                valid_urls.append(url)
        except requests.RequestException:
            pass
    return valid_urls

if __name__ == "__main__":
    test_urls = [
        "https://example.com/stream1.m3u8",
        "https://example.com/stream2.m3u8"
    ]
    valid = validate_m3u(test_urls)
    print("Enlaces válidos:", valid)
