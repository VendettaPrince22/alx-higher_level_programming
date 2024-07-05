#!/usr/bin/python3
"""Takes in a URL and email address, sends a POST and
displays the body of the response"""


if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    payload = {'email': sys.argv[2]}
    r = requests.post(url, data=payload)
    print(r.text)
