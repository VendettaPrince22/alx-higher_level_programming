#!/usr/bin/python3
"""Fetches 'https://alx-intranet.hbtn.io/status' """


if __name__ == "__main__":
    import urllib.request

    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(f'Body response:\n\t- type: {type(html)}')
        print(f'\t- content: {html}\n\t- utf8 content: {html.decode("utf-8")}')
