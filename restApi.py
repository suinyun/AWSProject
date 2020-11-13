import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('PII_Metadata')

def lambda_handler(event,context):
    print(event)
    mdID = event['ExpressionAttributeValues'][':v1']['S']
    response = table.get_item(
        Key={
            'ID': mdID
        }
    )
    resp = {"Bucket in S3": response["Item"]["Bucket in S3"], "File Name": response["Item"]["File Name"], "Path": response["Item"]["Path"],
        "Time Stamp": response["Item"]["Time Stamp"], "ID":response["Item"]["ID"], "PII Type": response["Item"]["PII Type"]}
    
    return resp