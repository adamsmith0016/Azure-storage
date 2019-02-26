from azure.storage.blob import BlockBlobService
import os
import sys
block_blob_service = BlockBlobService(account_name='', account_key='')
print("Retreiving blobs in specified container...")
blob_list=[]
container="containername"
countblob = 0
local_files = os.listdir(r'/home/user/test/newtest/testfolder')

print("************************Local files:************************ ")
print(local_files)
print("Number of Local Files:",len(local_files))

def list_blobs(container):
        try:

                global blob_list
                content = block_blob_service.list_blobs(container)
                print('\n' * 2)
                print("************************Blobs currently in the container:",container,"************************")
                for blob in content:

                        blob_list.append(blob.name)
                        print(blob.name)

        except:
                print("The specified container does not exist, Please check the container name or if it exists.")
list_blobs(container)
print("Number of files in the container:",len(blob_list))
#print("The list() is:")
#print(blob_list)

def Diff(local_files,blob_list):
    return(list(set(local_files) - set(blob_list)))
print('\n' * 2)
print("************************ Blobs NOT in the Azure Blob Storage are: ************************")
result=(Diff(local_files,blob_list))
print (result)

prompt = raw_input("Would you like to upload the files ? yes or no: ")

if prompt == "yes" or prompt == "y" or prompt == "YES":
        for file in result:
                block_blob_service.create_blob_from_path(container, file, file)
                print("File: ",file, "was uploaded")
#update content

#print(blob_list)
else:
        pass
list_blobs(container)
quest = raw_input("Would you like to delete local files? yes or no ?")
#Delete Local Files
if quest == 'yes' or quest == 'YES' or quest == 'y':
        for file in local_files:
                if file in blob_list:
                        if file == "compare-upload-delete.py":
                                continue
                        else:
                                os.remove(r'/home/user/test/newtest/testfolder'+file)
                                print("File: ", file,"Was Removed from Local DIR!")
                else:
                        print("File not yet in cloud:", file)
elif quest == 'no' or quest == 'NO' or quest == "n":
        print("No files will be deleted")
        sys.exit()

