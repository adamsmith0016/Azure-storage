# Azure-storage
This repo is meant to provide samples,templates, and quick & easy demos for Azure Storage: Files, Blobs etc... using python and the Azure Storage SDK. Please use at your own risk!

## Comparing Local files with the content of an Azure File Share(DIFF):

### Compare__AZFILES_Local.py:
Is a script allowing you to compare the content of a local directory(ex: “C:\Users\Desktop\test”(Windows) or "home/someuser"(Linux) etc..) to the content of an Azure File share. this also returns the local files that are NOT yet in the Azure File Share. It also filters the results by using basic string-matching ex “text” returns the file containing "text".

## How to list the content of a Blob Container, then delete a specific blob using Azure Blob Storage python SDK:

### del-blob.py:

The del-blob.py script allows you to list the blobs within a specific container(“containername”) then deletes a blob of your choice within it.
There are two types of blobs in this container, blobs within a virtual folder/path named “Virtual-Folder”, ex: “Virtual-Folder/Boards.png”, and blobs in the root of the container ex: “storage2.gif”
For the sake of simplicity, I added a list into which I collect the blob names from within the container, then, later would delete a chosen blob based on its index. 
In this example, I picked a blob to delete within a virtual folder: “Virtual-Folder/Boards.png”. Result of the script is below:


```python
  Retrieving blobs in specified container...
  ******Blobs currently in the container:**********
  Virtual-Folder/2019-02-06 10_43_04-Access Control - Microsoft Azure.png
  Virtual-Folder/Boards.png
  storage2.gif
  The list() of blobs is:
  ['Virtual-Folder/2019-02-06 10_43_04-Access Control - Microsoft Azure.png', 'Virtual-Folder/Boards.png', 'storage2.gif']
  ('Delete this blob: ', 'Virtual-Folder/Boards.png')
  ******Blobs currently in the container:**********
  Virtual-Folder/2019-02-06 10_43_04-Access Control - Microsoft Azure.png
  storage2.gif

```

## Comparing Local files with the content of a container in Azure Blob Storage:
### compare-upl-del-temp.py:
This script allows you to compare local files with the blobs in a container, then prints the Diff in between, uploads the local files which are not yet in the container, then deletes local files once they have been uploaded. It’s  similar to “print diff” between local files and container, then runs a “sync”: upload files present locally but not in the cloud, then deletes them from local storage.
**Arguments required from user:** Storage Account Name, Storage Account Key, Local directory path, and Container name.
**Note:** this script only works for files but not yet on folders.

Result example:

```python
Retreiving blobs in specified container...
************************Local files:************************
['compare-upload-delete.py', 'test.txt', 'test1.txt', 'test2.txt', 'test3.txt']



************************Blobs currently in the container:************************
Virtual-Folder/2019-02-06 10_43_04-Access Control - Microsoft Azure.png
compare-upload-delete.py
compareblob_loc.py
sol.py
test.txt



************************ Blobs NOT in the Azure Blob Storage are: ************************
['test3.txt', 'test1.txt', 'test2.txt']
('File: ', 'test3.txt', 'was uploaded')
('File: ', 'test1.txt', 'was uploaded')
('File: ', 'test2.txt', 'was uploaded')



************************Blobs currently in the container:************************
Virtual-Folder/2019-02-06 10_43_04-Access Control - Microsoft Azure.png
sol.py
test.txt
test1.txt
test2.txt
test3.txt
('File: ', 'test.txt', 'Was Removed from Local DIR!')
('File: ', 'test1.txt', 'Was Removed from Local DIR!')
('File: ', 'test2.txt', 'Was Removed from Local DIR!')
('File: ', 'test3.txt', 'Was Removed from Local DIR!')```
