#!/usr/bin/python3
"""Takes in a URL, sends a request and displays the body of response
"""


if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
