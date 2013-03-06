import os

import config

from boto.s3.connection import S3Connection
from boto.s3.key import Key

conn = S3Connection(
    config.AWS_ACCESS_KEY_ID, config.AWS_SECRET_ACCESS_KEY)
bucket = conn.create_bucket('stream2s3')

for dirpath, dirnames, filenames in os.walk(config.DESTINATION_DIRECTORY):
    print 'dirpath=', dirpath
    print 'dirnames=', dirnames
    print 'filenames=', filenames
    relpath = os.path.relpath(dirpath, config.DESTINATION_DIRECTORY)
    print 'relpath=', relpath
    for f in filenames:
        keyname = os.path.join(relpath, f)
        print 'keyname=', keyname
        filename = os.path.join(dirpath, f)
        print 'filename=', filename
        k = Key(bucket)
        k.key = keyname
        k.set_contents_from_filename(filename, replace=False)
