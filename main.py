import boto3
import sys
from copyfile import copy_object
s3_connect = boto3.resource("s3")
#print(f'files will be transferred from {sys.argv[1]} to {sys.argv[2]}')
def main():
    copy_object("bucket-kavyagm-1","IMG_20210206_180218.jpg", "bucket-kavyagm-2\/test")
    #copy_object("source bucketname", "object", Destination", "destination bucketname")

if __name__ == "__main__":
    main()


