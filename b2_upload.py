import os
from dotenv import load_dotenv
from b2sdk.v2 import InMemoryAccountInfo, B2Api

load_dotenv()

info = InMemoryAccountInfo()
b2_api = B2Api(info)

application_key_id = os.environ.get("B2_APP_KEY_ID")
application_key = os.environ.get("B2_APP_KEY")
b2_api.authorize_account("production", application_key_id, application_key)

ig_scheduler_bucket = b2_api.get_bucket_by_name("insta-bucket")

local_file_path = '/Users/mohdf/Downloads/12743835_1542484682711308_8189201039505577089_n.jpg'
b2_file_name = 'meme.jpg'
file_info = {'how': 'good-file'}

ig_scheduler_bucket.upload_local_file(
        local_file=local_file_path,
        file_name=b2_file_name,
        file_infos=file_info,
)
