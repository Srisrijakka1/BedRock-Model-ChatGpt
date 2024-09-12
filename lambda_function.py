import json
import boto3
def lambda_handler(event, context):
    input1 = event.get('queryStringParameters')
    input_question= list(input1)[0]
   
    # TODO implement
    #input_question = 'what is amazon bedrock?'
    bedrock_runtime = boto3.client('bedrock-runtime',region_name='us-east-1')
    response = bedrock_runtime.invoke_model(
            modelId = 'amazon.titan-text-premier-v1:0',
            body = json.dumps({'inputText':input_question})
        )
    body = json.loads(response.get('body').read())
    outputText = body.get('results')[0].get('outputText')
    return {
        'statusCode': 200,
        'body': json.dumps(str(outputText)),
        'headers':{
            'Content-Type':'application/json',
            'Access-Control-Allow-Origin':'*',
            'Access-Control-Allow-Methods':'PUT,POST,GET,OPTIONS',
            'Access-Control-Allow-headers':'Content-Type',
        }
    }
   