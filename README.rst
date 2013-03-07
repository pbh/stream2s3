Install streamripper::

    sudo apt-get install streamripper

Install required modules to virtualenv::

    pip install -r requirements.txt

Copy `config.sample.py` to `config.py` and edit it with required values. 
For instance, if you'd like to record for 4 hours set::

    NUMBER_OF_SECONDS_TO_RUN = 4 * 60 * 60

Update `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` there.

Check that the scripts are working (do it from virtualenv where requirements were installed)::

    python record_stream.py
    python upload_files.py

Set up commands to run with `crontab -e`. 
For example, the following lines will record starting at 20:00 every day, and upload every hour 
at 15 minutes past an hour starting at 20:15 and finishing at 00:15
(`-u` option so that logs may be checked as they are populated)::

    00 20 * * * cd /path/to/stream2s3 && /path/to/virtualenv/bin/python -u record_stream.py > /tmp/recordlog.txt 2>&1
    15 20 * * * cd /path/to/stream2s3 && /path/to/virtualenv/bin/python -u upload_files.py > /tmp/uploadlog.txt 2>&1
    15 21 * * * cd /path/to/stream2s3 && /path/to/virtualenv/bin/python -u upload_files.py > /tmp/uploadlog.txt 2>&1
    15 22 * * * cd /path/to/stream2s3 && /path/to/virtualenv/bin/python -u upload_files.py > /tmp/uploadlog.txt 2>&1
    15 23 * * * cd /path/to/stream2s3 && /path/to/virtualenv/bin/python -u upload_files.py > /tmp/uploadlog.txt 2>&1
    15 00 * * * cd /path/to/stream2s3 && /path/to/virtualenv/bin/python -u upload_files.py > /tmp/uploadlog.txt 2>&1
