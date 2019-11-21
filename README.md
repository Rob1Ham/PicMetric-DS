# Pic Metric 3 - Data Science API
Build on Deep Learning AMI (Amazon Linux) Version 25.3 - ami-028a41f747ffea9c0 using a g4dn.xlarge ec2 instance.

## Setup

Upon loading the server run the bootstrap.sh file, then create the .ev file.
Reference .env file, place in the Repo folder:

```
FLASK_ENV='development'
FLASK_APP='PicMetric:APP'

DATABASE_URL='postgres://Username:Password@URL:5432/table'

S3_KEY = 'KEYGOESHERE'
S3_SECRET = 'SECRETGOESHERE'
S3_BUCKET = 'BUCKETGOESHERE'
S3_LOCATION = 'http://BUCKETNAME.s3.amazonaws.com/'

ExtraArgs='{"ACL": "public-read", "ContentType": "image/png", "ContentDisposition": "inline"}'
```

To run the app, go into the Repo folder and run
`gunicorn -t 120 "PicMetric:create_app()"`
