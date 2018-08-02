#!/usr/bin/python3
""" script that takes in a string and sends a search request to the
    Star Wars API
"""
if __name__ == '__main__':
    import requests
    from sys import argv

    url = 'https://swapi.co/api/people/'
    payload = {"search": argv[1]}
    response = requests.get(url, params=payload).json()
    count = response["count"]
    print("Number of results: {}".format(count))
    if count > 0:
        for person in response["results"]:
            print(person["name"])
