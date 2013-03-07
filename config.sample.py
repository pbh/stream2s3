# streamripper options

STREAM_URL = 'http://www.wers.org/wers.pls'

# 15 minutes - 15 * 60
# 4 hours    - 4 * 60 * 60
NUMBER_OF_SECONDS_TO_RUN = 4 * 60 * 60

DESTINATION_DIRECTORY = '/tmp/stream2s3/'

# Required streamripper options are created from variables above
# more options may be specified in this variable directly.
# If -l, -d are mentioned they will override
# number of seconds and destination directory.
# This is not a good idea to include -d option
# because config.py value is used during upload.
# -s option so that subdirectory for a stream is not created
# --quiet so that no streaming output in log file
STREAMRIPPER_OPTIONS_STRING = '-s --quiet'


# Amazon S3 options

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

BUCKET_NAME = 'stream2s3'

# 100 Mb - 100 * 1024 ** 2
# 10 Gb  - 10 * 1024 ** 3
MAX_BUCKET_SIZE_BYTES = 100 * 1024 ** 2
