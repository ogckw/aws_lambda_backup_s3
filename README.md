# AWS Lambda Lab
## [繁體中文說明](#繁體中文說明) [English Guide](#english-guide)


# 繁體中文說明
[Demo1](#demo1-%E9%80%8F%E9%81%8Eaws-lambda-%E5%82%99%E4%BB%BDs3%E8%B3%87%E6%96%99-%E5%9C%A8%E6%AD%A4%E5%8E%9F%E5%A7%8B%E7%A2%BC%E6%A0%B9%E7%9B%AE%E9%8C%84) 透過AWS Lambda 備份S3資料

[Demo2](#demo2-%E6%94%B9%E8%AE%8A%E4%B8%8A%E5%82%B3%E7%9A%84%E5%9C%96%E7%89%87%E5%A4%A7%E5%B0%8F%E5%8F%8A%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8%E5%A5%97%E4%BB%B6-%E5%9C%A8%E6%AD%A4%E7%9B%AE%E9%8C%84%E5%BA%95%E4%B8%8B%E7%9A%84resize_image%E8%B3%87%E6%96%99%E5%A4%BE) 改變上傳的圖片大小及如何使用套件

## Demo1 透過AWS Lambda 備份S3資料 (在此原始碼根目錄)
透過AWS Lambda來備份S3檔案

Python 版本: 2.7
### 說明
範例程式將會透過放資料到S3上來驅動AWS Lambda執行，建議使用AWS有Admin權限的帳號來操作

工作流程如下:
上傳檔案 -> s3 bucket 1號 -> 驅動Lambda -> 複製檔案 -> 放到s3 bucket2號

使用的AWS服務:
1. AWS Lambda: 複製S3的檔案到另一個bucket中

2. AWS S3: 提供放入檔案的bucket驅動AWS Lambda後，輸出檔案到另一個bucket

3. AWS IAM Role: 分配AWS Lambda程式的權限能操作S3所有資源並有基本執行Lambda服務的權限


## Demo2 改變上傳的圖片大小及如何使用套件 (在此目錄底下的resize_image資料夾)

透過AWS Lambda改變圖片大小

Python 版本: 3.6

如何安裝Python套件

`pip install module-name -t /path/to/project-dir`

(如果是需要C或C++等需要Compile的套件，請使用AWS Linux image基底的作業系統compile

  請不要將Windows compile的套件上傳, 可參考 [Reference](#reference))
### 說明

![lambda architecture](lambda_file_processing.png)
使用AWS Lambda 轉換圖片成不同大小的圖片提供給各個裝置使用，建議使用AWS有Admin權限的帳號來操作

使用的AWS服務:
1. AWS Lambda: 轉換圖片成不同大小的圖片

2. AWS S3: 提供放入檔案的bucket驅動AWS Lambda後，輸出檔案到另一個bucket 

3. AWS IAM Role: 分配AWS Lambda程式的權限能操作S3所有資源並有基本執行Lambda服務的權限


# English Guide

[Demo1](#demo1-backup-s3-by-aws-lambda-root-directory) Backup S3 by AWS Lambda

[Demo2](#demo2-resize-image-and-how-to-deploy-new-module-resize_image)  Resize Image and How to Deploy New Module


## Demo1 Backup S3 by AWS Lambda (root directory)
Backup S3 by AWS Lambda
Python version: 2.7

### Description

This sample code will demo how to trigger AWS Lambda by putting object to AWS S3.
Please use AWS Admin account manipulate the tutorial

The workflow see below:

upload file -> s3 bucket1 -> trigger Lambda -> copy object -> s3 bucket2

Use AWS service:
1. AWS Lambda: copy s3 object to the other bucket

2. AWS S3: save input data, output data and trigger AWS Lambda

3. AWS IAM Role: assign AWS Lambda to full access s3 and basic execution


## Demo2 Resize Image and How to Deploy New Module (resize_image)

Resize image by AWS Lambda

Python version: 3.6

How to deploy new module

`pip install module-name -t /path/to/project-dir`

(if need compile by c or c++ , please use aws linux image compile.

  Do not use windows library upload, see [Reference](#reference))
  
### Description
![lambda architecture](lambda_file_processing.png)
Use AWS Lambda convert image to different size for multiple devices.
Please use AWS Admin account manipulate the tutorial

Use AWS service:
1. AWS Lambda: convert image from large to small

2. AWS S3: save input data, output data and trigger AWS Lambda

3. AWS IAM Role: assign AWS Lambda to full access s3 and basic execution

# Reference
- Tutorial by Node.js
http://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html

- Python or Node.js module compile OS version
http://docs.aws.amazon.com/lambda/latest/dg/current-supported-versions.html
