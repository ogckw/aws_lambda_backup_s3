import json
import boto3
from os.path import splitext
from PIL import Image
from io import BytesIO
from urllib.parse import unquote_plus

print('Loading function')
s3 = boto3.client('s3')

# resize and source folder path
# THUMBNAIL_SIZE = (250, 250)
SOURCE_BUCKET = 'hans-source-test'
RESIZE_BUCKET = 'hans-resize-test'
# mobile size , tablet size, com size
SIZE_LIST = [(320, 320), (768, 768), (1024, 1024)]
# resize folder
FOLDER_LIST = ['mobile', 'tablet', 'computer']

# choose right format extension


def file_extension(extension):
    if extension == 'JPEG':
        return 'jpg'
    elif extension == 'PNG':
        return 'png'
    else:
        return extension

# convert image size


def image_resize(image_source, resize_type):
    tmp = BytesIO()
    print('helper')
    image = Image.open(BytesIO(image_source))
    # print (image)
    image.thumbnail(resize_type)
    image.save(tmp, image.format)
    tmp.seek(0)
    output_data = tmp.getvalue()
    tmp.close()
    extension = file_extension(image.format)
    return output_data, extension

# lambda main function


def lambda_handler(event, context):
    # comment when production
    print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    print(bucket)
    key = unquote_plus(event['Records'][0]['s3']['object']['key'])
    print(key)
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        print(response)
        print("CONTENT TYPE: " + response['ContentType'])
        image_source = response['Body'].read()
        
        # filename and file content
        filename = splitext(key)[0]
        # iterator for upload three type of picture
        for ele in zip(SIZE_LIST, FOLDER_LIST):
            image_size = ele[0]
            folder_path = ele[1]
            resize_image = image_resize(image_source, image_size)
            resize_image_file = resize_image[0]
            resize_image_format = resize_image[1]
            s3_upload_key = folder_path + '/' + filename + '-resize.' + resize_image_format
            s3.put_object(Body=resize_image_file, Bucket=RESIZE_BUCKET, Key=s3_upload_key)
            print('Put object {} to s3 bucket {}'.format(key, bucket))
        return response['ContentType']
    except Exception as e:
        print(e)
        # print('Error getting object {} from bucket {}.
        # Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
