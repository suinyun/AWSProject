Macie Data Security Project

Motivation
The premise of this project was inspired by the feedbacks from customers of Amazon Macie, that it does not provide a convenient way for data engineers to investigate potential Data Loss Prevention (DLP) issues across a broad set of resources.

There are 3 python scripts in this repository - parsingMacieFindings.py, restApi.py, and cli.py. Respectively, the first script parses through Macie's findings and tags PII objects in S3 buckets, the second recieves REST API calls and retrieves metadata from Amazon DynamoDB table, and the third script provides a command line interface for client.  

Tech/framework used
The parsing and REST API python scripts are built with AWS Lambda. 

Features
The parsing function will parse through Macie's findings from Personal Identifiable Information (PII) inspection jobs for objects stored in S3. It will store the inspection job ID, object name, bucket name, PII type, time stamp, path of the object in S3, and other details of the metadata into a table in Amazon DynamoDB. 

The REST API function will take in the user's arguments passed in through API Gateway, and query the DynamoDB table accordingly. 

The CLI tool allows the user to make REST API calls from a client.

How to use
parsingMacieFindings.py
Run a Macie job into S3 buckets, then an Amazon CloudWatch event will trigger parsingMacieFindings.py to run.
restApi.py & cli.py
From client, run "python cli.py" and input the field name and the value as arguments you'd like to query the table by. The REST API call will trigger restApi.py to retrieve the right items from DynamoDB. 

How to edit
parsingMacieFindings.py
You can add additional or remove existing fields into the table by configuring the parsing Macie's findings portion of the script. Please make sure to update the "put_item()" part accordingly. You can also change how you'd like the PII objects in S3 to be tagged. For example, it can be {"PII Type": 'Financial Information'}
restApi.py
You can add additional or remove existing fields you'd like to query by adding/removing indexes in the DynamoDB table, then configuring the script accordingly with if/elif statements.
cli.py
You can add more help statements or more arguments in order to be able to query more than once without re-running the script.

