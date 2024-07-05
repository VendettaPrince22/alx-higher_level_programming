#!/usr/bin/python3
"""Takes in a letter and sends a POST to a URL with letter as param"""


if __name__ == "__main__":
    import sys
    import requests

    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 3:
        payload = {'q': sys.argv[2]}
    else:
        payload = {'q': ""}

    r = requests.post(url, data=payload)
    try:
        my_dict = r.json()
        if len(my_dict) == 0:
            print("No result")
        else:
            print("[{}] {}".format(my_dict.get('id'), my_dict.get('name')))
    except ValueError:
        print("Not a valid JSON")
