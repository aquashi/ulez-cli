import argparse
import json
import requests


parser = argparse.ArgumentParser(description='Check if vehicle is ULEZ compliant using TfL Unified API')
parser.add_argument('-p', '--plate', metavar='AB12CDE',
                    help='enter UK licence plate without spaces (e.g. AB12CDE)', type=str, required=True)
parser.add_argument('-d', '--detail', help="request additional vehicle details", action='store_true')
args = parser.parse_args()

def check(plate, detail=False):
    # test compliant plate = 'DU64HSO'
    # test non-compliant plate = 'GU57YCP'
    plate = plate
    detail = detail
    url = f'https://82vqql5ek8.execute-api.eu-west-2.amazonaws.com/live/plate?vrm={plate}'
    req = requests.get(url)
    try:
        req_json = req.json()     
    except:
        return print('Connection Error: Check API credentials and/or internet connection')
    try:
        if detail is True:
            del req_json['$type']
            del req_json['type']
            st_json = json.dumps(req_json, indent=2)
            return print(f'{st_json}')
        else:
            return print(f'"compliance": "{req_json["compliance"]}"')
    except TypeError:
        return print('Invalid Licence Plate')

if __name__ == "__main__":
    check(args.plate, args.detail)