#!/usr/bin/env python3

import argparse
import urllib.request
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
            contents = urllib.request.urlopen(target_url).read()
        except urllib.error.HTTPError as e:
            print(f'error: {e.reason}')
        except urllib.error.URLError as e:
            print(f'error: {e.reason}')
        else:
            json_data = json.loads(contents.decode("utf-8").replace("'", '"'))
            print(json.dumps(json_data, indent=4, sort_keys=True))


