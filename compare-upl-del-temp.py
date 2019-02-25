from azure.storage.blob import BlockBlobService
import os
block_blob_service = BlockBlobService(account_name='Storageaccountname', account_key='Storage Account Key')
print("Retreiving blobs in specified container...")
blob_list=[]
container="Your_containername"

local_files = os.listdir(r'/home/SOMEUSER/directory/')

print("************************Local files:************************ ")
print(local_files)

def list_blobs(container):
        try:

                global blob_list
                content = block_blob_service.list_blobs(container)
		print('\n' * 2)
                print("************************Blobs currently in the container:************************")
                for blob in content:
                        blob_list.append(blob.name)
                        print(blob.name)
        except:
                print("The specified container does not exist, Please check the container name or if it exists.")
list_blobs(container)
#print("The list() is:")
#print(blob_list)

def Diff(local_files,blob_list):
    return(list(set(local_files) - set(blob_list)))
print('\n' * 2)
print("************************ Blobs NOT in the Azure Blob Storage are: ************************")
result=(Diff(local_files,blob_list))
print (result)


for file in result:
    block_blob_service.create_blob_from_path(container, file, file)
    print("File: ",file, "was uploaded")
#update content
list_blobs(container)
#print(blob_list)
#Delete Local Files
for file in local_files:
    if file in blob_list:
	if file == "compare-upload-delete.py":
		continue
	else:
        	os.remove(r'/home/SOMEUSER/directory/'+file)
        	print("File: ", file,"Was Removed from Local DIR!")
    else:
	print("File not yet in cloud:", file)
        

