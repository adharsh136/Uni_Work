import boto3

#Bucket configuration
name = '23796349-lab8'
bucket_config = {'LocationConstraint': 'ap-northeast-2'} 

#S3 client
s3 = boto3.client("s3")

try:
    s3.create_bucket(Bucket=name,CreateBucketConfiguration=bucket_config) #create_bucket function is idempotent.
    response = s3.head_bucket(Bucket=name)
    print(f"Bucket '{name}' created and exists.")
    print(response)
except Exception as error:
    pass

