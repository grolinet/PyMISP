#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymisp import PyMISP
from keys import url_priv, key_priv
# from keys import url_cert, key_cert
import argparse


# Usage for pipe masters: ./last.py -l 5h | jq .


def init(url, key):
    return PyMISP(url, key, True, 'json')


def up_event(m, event, content):
    with open(content, 'r') as f:
        result = m.update_event(event, f.read())
    print result.text

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get an event from a MISP instance.')
    parser.add_argument("-e", "--event", required=True, help="Event ID to get.")
    parser.add_argument("-i", "--input", required=True, help="Input file")

    args = parser.parse_args()

    misp = init(url_priv, key_priv)
    # misp = init(url_cert, key_cert)

    up_event(misp, args.event, args.input)
