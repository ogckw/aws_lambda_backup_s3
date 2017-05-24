# aws_lambda_backup_s3
For demo AWS Lambda trigger

[Description]
This sample code will demo how to trigger AWS Lambda by putting object to AWS S3.

[Workflow]
upload file -> s3 bucket1 -> trigger Lambda -> copy object -> s3 bucket2


# Demo and how to deploy new module

how to deploy new module

pip install module-name -t /path/to/project-dir

(if need compile by c or c++ , please use aws linux image compile.

  Do not use windows library upload, see reference)

[Demo]
Detect every 5 minute's top 5 news category

AWS service to crawler and parser data

1. AWS Lambda : Crawl and parser data.

2. AWS CloudWatch : Set schedule.

3. AWS S3 : Save input data, output data and trigger AWS Lambda.

4. IAM role : assign AWS Lambda to full access s3 and basic execution

[Reference]
tutorial by node.js

http://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html

python module compile os

http://docs.aws.amazon.com/lambda/latest/dg/current-supported-versions.html
