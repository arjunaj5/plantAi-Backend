
from imagekitio import ImageKit


def upload_to_imagekit(base64):
    imagekit = ImageKit(
        public_key='public_w+kNN4IBgs9XvvNu2dJSVU5l7VU=',
        private_key='private_MAczB8S91roeyMBun0AgJEjlh2Y=',
        url_endpoint='https://ik.imagekit.io/plantAi'
    )
    upload = imagekit.upload(
        file=base64,
        file_name="detections",
        options={
            "folder": "/detections"
        },
    )
    return upload['response']['url']
