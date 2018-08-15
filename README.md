# Some notes for running lambdas using python and pipenv

## creating requirements.txt
pipenv run pip freeze > requirements.txt

## uploading file to s3 / triggering the event
aws s3 cp users.json s3://peterh-sydney-data-lake

## Checking the logs
sls logs -f hello