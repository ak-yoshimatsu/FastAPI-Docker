import boto3

s3 = boto3.client(
    "s3",
    # endpoint_url="http://127.0.0.1:9000",
    endpoint_url="http://localhost:9000",
    aws_access_key_id="rootroot",
    aws_secret_access_key="secretsecret",
)
response = s3.list_buckets()
print(response["Buckets"])

s3.create_bucket(Bucket="from-boto")

response = s3.list_buckets()
print(response["Buckets"])
