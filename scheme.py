from pydantic import BaseModel

class IamReq(BaseModel):
    access_key: str
    secret_key: str
    profile: str

class Ec2Req(BaseModel):
    profile: str