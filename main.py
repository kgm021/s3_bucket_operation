import boto3
import sys
from copyfile import copy_object
from copyfile import delete_existing_object
s3_connect = boto3.resource("s3")
print(f'files will be transferred from {sys.argv[1]} to {sys.argv[3]}')
SourceBucketName = sys.argv[1]
FileToCopy = sys.argv[2]
DestinationBucket = sys.argv[3]
def main():
    copy_object(SourceBucketName, FileToCopy, DestinationBucket)
    #copy_object("source bucketname", "object", Destination", "destination bucketname")
    delete_existing_object(SourceBucketName, FileToCopy)

if __name__ == "__main__":
    main()


