import shlex
from subprocess import call
import datetime

import config


# creating list of options

options_str = config.STREAM_URL + ' ' + config.STREAMRIPPER_OPTIONS_STRING

# destination directory
if not '-d' in options_str and config.DESTINATION_DIRECTORY:
    options_str += ' -d {0}'.format(config.DESTINATION_DIRECTORY)

# number of seconds to run
if not '-l' in options_str and config.NUMBER_OF_SECONDS_TO_RUN:
    options_str += ' -l {0}'.format(config.NUMBER_OF_SECONDS_TO_RUN)

options_list = shlex.split(options_str)


# running streamripper

print 'starting recording: {}'.format(datetime.datetime.now())
print 'options used to run: {}'.format(options_str)

call(['streamripper'] + options_list)

print 'finished recording: {}'.format(datetime.datetime.now())
