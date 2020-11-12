####### import statements #######
import json
import boto3
import sys
import time

####### calling s3 and dynaboDB #######
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
dynamodb_client = boto3.client('dynamodb')

def lambda_handler(event, context):
    
    #### accesses the metaData from Macie Finding ####
    ID = event['id']
    # print(ID)
    timeStamp = event['time']
    bucketName = event['detail']['resourcesAffected']['s3Bucket']['name']#s3 bucket name
    # print(bucketName)
    s3fileName = event['detail']['resourcesAffected']['s3Object']['key']#s3 object name
    # print(s3fileName)
    details = event['detail']['classificationDetails']['result']['sensitiveData']
    # print(details)
    path = event['detail']['resourcesAffected']['s3Object']['path']
    # print(path)
    verID = event['detail']['resourcesAffected']['s3Object']['versionId']
    piiType = event['detail']['classificationDetails']['result']['sensitiveData'][0]['category']

    table = dynamodb.Table('PII_Metadata')
    print("PII_Metadata table found in DynamoDB")
    
    ##### enters data into the table #######
    table.put_item(
        Item={
            'ID' : ID,
            'Time Stamp' : timeStamp,
            'File Name' : s3fileName,
            'Bucket in S3' : bucketName,
            'Details' : details,
            'Path' : path,
            'PII Type' : piiType
        }
    )
    print("done!")
    
    #### object tagging in S3 ####
    ## data classifcation as the name of the tag
    response = s3_client.put_object_tagging(
        Bucket = bucketName,
        Key = s3fileName,
        VersionId = verID,
        Tagging = {
            'TagSet': [
                {
                    'Key': "data_classification",
                    'Value': 'pii'
                },
            ]
        }
    )
    # print(response)