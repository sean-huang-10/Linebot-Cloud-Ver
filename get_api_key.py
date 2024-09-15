from google.cloud import storage

def get_api_key(key_name):
    bucket_name = 'linebot-cls'
    source_blob_name = key_name  # 替換成你具體的文件路徑

    # 初始化 Cloud Storage 客戶端
    storage_client = storage.Client()

    # 获取存储桶和 blob 对象
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    # 读取文件内容
    file_content = blob.download_as_text()
    # 返回文件内容
    return file_content
