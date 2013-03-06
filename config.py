# streamripper options

STREAM_URL = 'http://www.wers.org/wers.pls'

NUMBER_OF_SECONDS_TO_RUN = 10

DESTINATION_DIRECTORY = '/tmp/stream2s3/'

# required streamripper options are created from variables above
# more options may be specified in this variable directly
# if -l, -d are mentioned they override
# number of seconds and destination directory
# -s option so that subdirectory for a stream is not created
STREAMRIPPER_OPTIONS_STRING = '-s'
