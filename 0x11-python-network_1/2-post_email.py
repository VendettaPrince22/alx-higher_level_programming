#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request to passed URL
with the email as a parameter, and displays the response body"""


if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    import sys

    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print(content.decode('utf-8'))
