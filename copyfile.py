import boto3
import sys
s3_connect = boto3.resource("s3")
#print(f'files will be transferred from {sys.argv[1]} to {sys.argv[2]}')
def copy_object(SourceBucketName, FileToCopy, DestinationBucket):
    copy_source = {
    'Bucket': SourceBucketName,
    'Key' : FileToCopy
    }
    bucket = s3_connect.Bucket(DestinationBucket)
    bucket.copy(copy_source, DestinationBucket)


    