# io_examples/reqs_post.py
import requests


url = "https://httpbin.org/post"
data = dict(title="Learn Python Programming")


resp = requests.post(url, data=data)
print("Response for POST")
print(resp.json())


"""
$ python reqs_post.py

Response for POST
{
    "args": {},
    "data": "",
    "files": {},
    "form": {"title": "Learn Python Programming"},
    "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Content-Length": "30",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "httpbin.org",
        "User-Agent": "python-requests/2.25.1",
        "X-Amzn-Trace-Id": "Root=1-60a43131-5032cdbc14db751fe775",
    },
    "json": None,
    "origin": "86.8.174.15",
    "url": "https://httpbin.org/post",
}
"""
