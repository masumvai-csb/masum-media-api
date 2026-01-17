"""
========================================
 Author   : Masum Vai
 Channel  : https://t.me/masum_tech_sensei
 Note     : Coded with by Masum Vai
========================================
"""

import json
import requests

def handler(request):
    author = "Masum Vai"
    channel = "https://t.me/masum_tech_sensei"

    vd = request.args.get("vd")

    if not vd:
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "status": "error",
                "author": author,
                "channel": channel,
                "message": "Missing required parameter: vd"
            }, indent=2)
        }

    api_url = "https://allmedia-dl.vercel.app/download?url=" + vd

    try:
        r = requests.get(api_url, timeout=20)

        if r.status_code != 200:
            raise Exception("Original API failed")

        data = r.json()

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "status": "success",
                "author": author,
                "channel": channel,
                "data": data
            }, indent=2)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "status": "error",
                "author": author,
                "channel": channel,
                "message": str(e)
            }, indent=2)
            }
