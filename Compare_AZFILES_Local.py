import os
import azure.storage.common
from azure.storage.common import CloudStorageAccount
from azure.storage.file import FileService
file_service = FileService(account_name='storage_acct_name', account_key='keyhere')


local_files = os.listdir(r'/home/User/storage-file')
print("Local files: ")
print(local_files)

print('Azure Files in the Cloud:')
files_incloud= list()

generator = file_service.list_directories_and_files('filesharename')
for file_or_dir in generator:
        files_incloud.append(file_or_dir.name)
        print(file_or_dir.name)

def Diff(local_files,files_incloud):
    return(list(set(local_files) - set(files_incloud)))

print("Files NOT in the Cloud FILESHARE are: ")
result=(Diff(local_files,files_incloud))
print (result)
print("\n")
print("Matching Strings:")
print("\n")
for item in result:
        if "text" in item:
                print item

