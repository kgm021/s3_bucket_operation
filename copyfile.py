import boto3

s3_connect = boto3.resource("s3")

def copy_object(SourceBucketName, FileToCopy, DestinationBucket):
    copy_source = {
    'Bucket': SourceBucketName,
    'Key' : FileToCopy
    }
    bucket = s3_connect.Bucket(DestinationBucket)
    bucket.copy(copy_source, DestinationBucket)

def delete_existing_object(SourceBucketName, FileToCopy):
    s3_connect.Object(SourceBucketName, FileToCopy).delete()