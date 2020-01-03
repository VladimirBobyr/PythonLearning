import requests
import json

def lambda_handler(event, context):
    # TODO implement
    link_page = "https://career.deutsche-boerse.com/job/Prague-DevOps-Engineer-in-Regulatory-%28mfd%29-108/530959601/" #85172
    inside_page = requests.get(link_page)
    print(len(inside_page.text))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

lambda_handler(1,1)
