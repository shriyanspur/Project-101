import dropbox
import os

class TransferData:
  def __init__(self, access_token):
    self.access_token = access_token

  def upload_File(self, file_from, file_to):
    dbx = dropbox.Dropbox(self.access_token)

    f = open(file_from, 'rb')
    
    dbx.files_upload(f.read(), file_to)

def main():
  token = input('Input your dropbox access token: ')

  access_token = token
  transferData = TransferData(access_token)

  file_from = input('Enter the folder location: ')
  name = input('Enter folder name to be created: ')

  fileList = os.listdir(file_from)

  for file in fileList:
    file_to = '/' + name + '/' + file

    transferData.upload_File(file, file_to)
    print(file, 'has been moved')

main()