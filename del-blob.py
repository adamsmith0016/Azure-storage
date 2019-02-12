#ref = https://stackoverflow.com/questions/49387388/how-do-i-delete-a-folderblob-inside-an-azure-container-using-delete-blob-metho
from azure.storage.blob import BlockBlobService
#import azure.storage.blob
block_blob_service = BlockBlobService(account_name='yraccountname', account_key='accountkey')
print("Retreiving blobs in specified container...")
blob_list=[]
container="containername"
def list_blobs(container):
        try:

                global blob_list
                content = block_blob_service.list_blobs(container)
                print("******Blobs currently in the container:**********")
                for blob in content:
                        blob_list.append(blob.name)
                        print(blob.name)
        except:
                print("The specified container does not exist, Please check the container name or if it exists.")
list_blobs(container)
print("The list() is:")
print(blob_list)
print("Delete this blob: ",blob_list[1])
#DELETE A SPECIFIC BLOB FROM THE CONTAINER
block_blob_service.delete_blob(container,blob_list[1],snapshot=None)
list_blobs(container)

#RESULT:
#Retreiving blobs in specified container...
# ******Blobs currently in the container:**********
# Virtual-Folder/2019-02-06 10_43_04-Access Control - Microsoft Azure.png
# Virtual-Folder/Boards.png
# storage2.gif
# The list() is:
# ['Virtual-Folder/2019-02-06 10_43_04-Access Control - Microsoft Azure.png', 'Virtual-Folder/Boards.png', 'storage2.gif']
# ('Delete this blob: ', 'Virtual-Folder/Boards.png')
# ******Blobs currently in the container:**********
# Virtual-Folder/2019-02-06 10_43_04-Access Control - Microsoft Azure.png
# storage2.gif
