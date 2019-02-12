# Azure-storage
This repo is meant to provide samples, examples and quick & easy demos for Azure Storage: Files, Blobs etc... using python and the Azure Storage SDK.

## Comparing Local files with the content of an Azure File Share:

### Compare__AZFILES_Local.py:
Is a script allowing you to compare the content of a local directory(ex: “C:\Users\Desktop\test”(Windows) or "home/someuser"(Linux) etc..) to the content of an Azure File share. this also returns the local files that are NOT yet in the Azure File Share. It also filters the results by using basic string-matching ex “text” returns the file containing "text".

## How to list the content of a Blob Container, then delete a specific blob using Azure Blob Storage python SDK:

### del-blob.py

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
