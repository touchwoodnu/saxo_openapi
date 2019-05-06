# -*- coding: utf-8 -*-


def read_token(tokenFile="token.txt"):
    with open(tokenFile) as FHtok:
        token = FHtok.read().strip()
        if not token:
            print("Please set it up correctly: see index.ipynb")

        return token


def request_info(r):
    """request_info = show some information for request instance r."""
    print("API-endpoint   : {}".format(r))
    print("METHOD         : {}".format(r.method))
    print("Response status: {}".format(r.status_code))
