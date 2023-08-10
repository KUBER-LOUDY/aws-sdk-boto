import json
import boto3
import os
import subprocess
import scheme
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", "http://localhost:3000"],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*", "access-token", "access_token", "Authorization"],
    allow_credentials=False
)

@app.post("/iam/regist")
async def regist_iam_user(req: scheme.IamReq):
    os.system("aws configure set aws_access_key_id " + req.access_key +" --profile " + req.profile)
    os.system("aws configure set aws_secret_access_key " + req.secret_key + " --profile " + req.profile)
    os.system("aws configure set region ap-northeast-2 --profile " + req.profile)
    
    
@app.post("/ec2/start")
async def create_standard_ec2(req: scheme.Ec2Req):
    os.environ['AWS_PROFILE'] = req.profile
    client = boto3.client('ec2', region_name='ap-northeast-2')

    response = client.run_instances(
        ImageId='ami-0c9c942bd7bf113a2',
        InstanceType='t2.micro',
        MaxCount=1,
        MinCount=1,
        Monitoring={
            'Enabled': False
        },
    )
    
    return response