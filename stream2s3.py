import config
import shlex
from subprocess import call

options_str = config.STREAM_URL + ' ' + config.STREAMRIPPER_OPTIONS_STRING

if not '-d' in options_str and config.DESTINATION_DIRECTORY:
    options_str += ' -d {0}'.format(config.DESTINATION_DIRECTORY)

if not '-l' in options_str and config.NUMBER_OF_SECONDS_TO_RUN:
    options_str += ' -l {0}'.format(config.NUMBER_OF_SECONDS_TO_RUN)

options_list = shlex.split(options_str)
print options_list
call(['streamripper'] + options_list)
