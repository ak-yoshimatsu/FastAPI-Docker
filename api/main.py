from fastapi import FastAPI

import boto3


app = FastAPI()


@app.get('/')
def index():
    return {'data': 'Hello!!!'}


@app.get('/minio')
def operate():
    s3 = boto3.client(
        's3',
        endpoint_url='http://127.0.0.1:9000',
        # endpoint_url='http://localhost:9000',
        # endpoint_url='http://localhost:9001',
        # aws_access_key_id='mXRZWaHNQyG8YXAPRUqQ',
        # aws_secret_access_key='aoV7MfpIhKyHHUH9hYDicbzqsqvhHxiAKaJXYf5U',
        aws_access_key_id='rootroot',
        aws_secret_access_key='secretsecret',
    )

    # バケット作成
    response = s3.list_buckets()
    print(response["Buckets"])

    s3.create_bucket(Bucket="from-boto")

    response = s3.list_buckets()
    print(response["Buckets"])

    # # minioのバケット出力
    # print('バケット一覧')
    # for bucket in s3.buckets.all():
    #     print(bucket.name)
    # print('')

    # # minio内のREADME.mdの出力
    # print('README.mdの出力')
    # obj = s3.Object('aaaaaaaaaaaaaaaaaaaaaaa', 'README.md')
    # res = obj.get()
    # print(res['Body'].read().decode())
