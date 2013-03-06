based on gist: https://gist.github.com/pbh/bb71b4fb9083c70cda5e

User story
~~~~~~~~~~

1. A user may start the script.

Script:

- records stream (saves to /tmp) for time specified in `config.py`
  - other options for streamripper may also be specified in `config.py`
- checks space in S3 bucket (bucket name, and credentials are specified in `config.py`
  - if not enough space deletes old files (maximum space is in `config.py`)
- uploads the recording

2. A user may run the script with cron.

- Sample command in `README.rst`.


Requirements
~~~~~~~~~~~~

1. Everything needs to be runnable on Ubuntu 12.04.1. (And you should have something close enough to that to be able to test on.)
2. You will need to use a requirements.txt and a virtualenv for your Python script.
3. You will need to use boto (or similar) for S3 access, installable in the virtualenv.
4. You will need to use streamripper (or similar) for downloading the shows as they play live each day.
5. You should not use any long term storage on the Ubuntu machine (other than for the script). Any metadata about file sizes or what shows are on S3 should also be stored on S3. You can assume that you have temporary storage for storing the show as you download it (e.g., in /tmp), but that you want to move it to S3 as quickly as possible.
6. You should have your own S3 bucket so that you can get things running on your own and so that I can just check your S3 bucket to make sure things are working. (I'll switch it to use my own S3 settings once you are done.)
7. Ideally: you should be familiar with Github and keep a repository for the script --- it's fine if this is a public repository.
