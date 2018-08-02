#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL and displays
    the body of the response (decoded in utf-8)
"""
if __name__ == '__main__':
    import sys
    import urllib.request

    request = urllib.request.Request(sys.argv[1])

    try:
        response = urllib.request.urlopen(request)
        print(response.read().decode(encoding='utf-8'))
    except Exception as error:
        print('Error code: {}'.format(error.getcode()))
