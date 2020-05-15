#!/usr/bin/env python3

import argparse
import requests
import json

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('filename')
arg_parser.add_argument('--path', type=str)
args = arg_parser.parse_args()

with open(args.filename) as f:
    for ip in f.readlines():
        target_url = f"http://{ip.rstrip()}{args.path}"
        print(f"\ncalling: {target_url}")

        try:
            contents = requests.get(target_url)
        except requests.exceptions.HTTPError as err:
            print("Http Error:",err)
        except requests.exceptions.ConnectionError as err:
            print("Connection Error:",err)
        except requests.exceptions.Timeout as err:
            print("Timeout Error:",err)
        except requests.exceptions.RequestException as err:
            print("Error:",err)
        else:
            print(json.dumps(contents.json(), indent=4, sort_keys=True))


