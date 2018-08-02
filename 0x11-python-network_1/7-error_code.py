#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL and displays
    the body of the response
"""
if __name__ == '__main__':
    import sys
    import requests

    try:
        response = requests.get(sys.argv[1])
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError as error:
        print('Error code: {}'.format(error.response.status_code))
