# io_examples/reqs.py
import requests


urls = {
    "get": "https://httpbin.org/get?t=learn+python+programming",
    "headers": "https://httpbin.org/headers",
    "ip": "https://httpbin.org/ip",
    "user-agent": "https://httpbin.org/user-agent",
    "UUID": "https://httpbin.org/uuid",
    "JSON": "https://httpbin.org/json",
}


def get_content(title, url):
    resp = requests.get(url)
    print(f"Response for {title}")
    print(resp.json())


for title, url in urls.items():
    get_content(title, url)
    print("-" * 40)


"""
$ python reqs.py

Response for get
{
    "args": {"t": "learn python programming"},
    "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Host": "httpbin.org",
        "User-Agent": "python-requests/2.25.1",
        "X-Amzn-Trace-Id": "Root=1-60a42902-3b6093e26ae375244478",
    },
    "origin": "86.8.174.15",
    "url": "https://httpbin.org/get?t=learn+python+programming",
}
----------------------------------------
Response for headers
{
    "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Host": "httpbin.org",
        "User-Agent": "python-requests/2.25.1",
        "X-Amzn-Trace-Id": "Root=1-60a42902-69f2988c72187527c7aa",
    }
}
----------------------------------------
Response for ip
{'origin': '86.8.174.15'}
----------------------------------------
Response for user-agent
{'user-agent': 'python-requests/2.25.1'}
----------------------------------------
Response for UUID
{'uuid': '008df02c-6e62-4c88-97ad-3c3604998273'}
----------------------------------------
Response for JSON
{
    "slideshow": {
        "author": "Yours Truly",
        "date": "date of publication",
        "slides": [
            {"title": "Wake up to WonderWidgets!", "type": "all"},
            {
                "items": [
                    "Why <em>WonderWidgets</em> are great",
                    "Who <em>buys</em> WonderWidgets",
                ],
                "title": "Overview",
                "type": "all",
            },
        ],
        "title": "Sample Slide Show",
    }
}
----------------------------------------
"""
