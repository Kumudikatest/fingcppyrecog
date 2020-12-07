import boto3
rekognition = boto3.client("rekognition")

def handler(request):
    try:
        data = rekognition.compare_faces(
            SourceImage={
                'S3Object': {
                    'Bucket': "cloud9-ktest",
                    'Name': "AS2station.png"
                }
            },
            TargetImage={
                'S3Object': {
                    'Bucket': "cloud9-ktest",
                    'Name': "shot-buffalo-5daeeb9351a540214a19d115-wiu.png"
                }
            }
        )
    except BaseException as e:
        print(e)
        raise(e)
        print("Test")
    
    return "Successfully executed"
