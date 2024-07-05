#!/usr/bin/python3
"""Takes in a URL, sends a request and displays the value of
X-Request_Id variable in the header of response"""


if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        header = response.headers._headers
        for i in header:
            if 'X-Request-Id' in i:
                print(i[1])
