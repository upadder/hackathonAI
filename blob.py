from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

connection_string = "DefaultEndpointsProtocol=https;AccountName=georgehackathonstorage;AccountKey=jYAX+Svb+aH1PVuHYkz76/XDSSS2BPAPwQ9J/n85EOZMVC/A0xnDQyvkYfd7t6Hj/37gOhzS/h0k+AStBfl8OA==;EndpointSuffix=core.windows.net"  #
container_name = "stonybrookcontainer"
blob_name = "georgehackathonstorage"
directory_path = "Data"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

for root, dirs, files in os.walk(directory_path):
    for file in files:
        file_path = os.path.join(root, file)
        blob_name = os.path.relpath(file_path, directory_path)

        blob_client = blob_service_client.get_blob_client(
            container=container_name, blob=blob_name
        )

        with open(file_path, "rb") as data:
            blob_client.upload_blob(data,overwrite=True)

        print(f"date {file_path} uploaded {blob_name} hurray!")
