#!/usr/bin/python3
"""Takes in a URL, sends a request and displays the value of the
variable 'X-Request-Id' in response header"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))
