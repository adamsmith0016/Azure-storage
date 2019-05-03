from azure.storage.blob import BlockBlobService
block_blob_service = BlockBlobService(account_name='storageaccountname', account_key='StorageaccountKey')
#provide specific blob to read
file = block_blob_service.get_blob_to_text('containername', 'blobname')
content = file.content
#print blob's content
print(content)
