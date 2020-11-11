import argparse
import sys
import requests

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Welcome to Suin's Project Demo! Please provide what field and value" +
        "you'd like to query the PII_Metadata table.")
    parser.add_argument("field")
    parser.add_argument("value")
    args = parser.parse_args()
    field = args.field
    if field == "ID":
        print ('Yes')
    value = args.value
    url = 'https://ni5m1df3eg.execute-api.us-east-1.amazonaws.com/test/pii-metadata?'
    urlNargs = url+field+"="+value

    sample_api_key = '0d7441d4-82a6-8b79-8569-dd4f7553614b'
    response = requests.get(urlNargs, params=sample_api_key)
    print(response.json())  