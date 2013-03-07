import os

from boto.s3.connection import S3Connection
from boto.s3.key import Key

import config


# connection to bucket

conn = S3Connection(
    config.AWS_ACCESS_KEY_ID, config.AWS_SECRET_ACCESS_KEY)

bucket = conn.create_bucket(config.BUCKET_NAME)


# upload files
print 'Uploading from {}\n'.format(config.DESTINATION_DIRECTORY)

for dirpath, dirnames, filenames in os.walk(config.DESTINATION_DIRECTORY):
    relpath = os.path.relpath(dirpath, config.DESTINATION_DIRECTORY)
    for f in filenames:
        keyname = os.path.join(relpath, f)
        filename = os.path.join(dirpath, f)
        k = Key(bucket)
        k.key = keyname
        print 'uploading: {}'.format(keyname)
        k.set_contents_from_filename(filename, replace=False)


# check bucket size and clean old files if necessary

total_bucket_size = 0
for key in bucket:
    total_bucket_size += key.size

Mb = 1024 ** 2
print
print 'Total bucket size (Mb): {0:.2f}'.format(total_bucket_size / float(Mb))
print 'Maximum size specified in congif.py (Mb): {0:.2f}'.format(
    config.MAX_BUCKET_SIZE_BYTES / float(Mb))

if total_bucket_size > config.MAX_BUCKET_SIZE_BYTES:
    print
    print 'Cleaning bucket (oldest files first)\n'
    new_total_bucket_size = total_bucket_size
    count_deleted = 0
    for key in sorted(bucket, key=lambda x: x.last_modified):
        new_total_bucket_size -= key.size
        bucket.delete_key(key)
        print 'deleted: {}'.format(key.name)
        count_deleted += 1
        if new_total_bucket_size <= config.MAX_BUCKET_SIZE_BYTES:
            print
            print 'Number of keys deleted: {}'.format(count_deleted)
            print 'Total bucket size after clean up (Mb): {0:.2f}'.format(
                new_total_bucket_size / float(Mb))
            break
