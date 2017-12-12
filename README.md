# Demo1 backup S3 by AWS Lambda (root directory)
Backup S3 by AWS Lambda
Python version: 2.7

## Description

This sample code will demo how to trigger AWS Lambda by putting object to AWS S3.

The workflow see below:

upload file -> s3 bucket1 -> trigger Lambda -> copy object -> s3 bucket2

# Demo2 resize_image how to deploy new module (resize_image)

Resize image by AWS Lambda

Python version: 3.6

How to deploy new module

pip install module-name -t /path/to/project-dir

(if need compile by c or c++ , please use aws linux image compile.

  Do not use windows library upload, see [Reference](#reference))
  
## Description
![lambda architecture](lambda_file_processing.png)
Use AWS Lambda convert image from large to small

Use AWS service:
1. AWS Lambda: convert image from large to small

2. AWS S3: save input data, output data and trigger AWS Lambda

3. AWS IAM Role: assign AWS Lambda to full access s3 and basic execution


# Demo3 how to deploy new module (apple_news)

How to deploy new module

pip install module-name -t /path/to/project-dir

(if need compile by C or C++ , please use AWS Linux image compile.

  Do not use Windows library upload, see [Reference](#reference))
  
## Description
Detect every 5 minute's top 5 news category

AWS service to crawler and parser data

Use AWS Service: 

1. AWS Lambda: crawl and parser data

2. AWS CloudWatch: set schedule

3. AWS S3: save input data, output data and trigger AWS Lambda

4. AWS IAM role : assign AWS Lambda to full access s3 and basic execution

# Reference
- Tutorial by Node.js
http://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html

- Python or Node.js module compile OS version
http://docs.aws.amazon.com/lambda/latest/dg/current-supported-versions.html
