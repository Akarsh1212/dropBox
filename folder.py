import os
import dropBox
from dropBox.files import WriteMode
class TransferData:
    def __init__ (self , access_token):
        self.access_token = access_token
    def upload_file (self, file_from , file_to):
        dbx = dropBox.Dropbox(self.access_token)
        for root, dirs files in os.walk(file_from):
            for fileName in files :
                local_Path  = os.path.join(root, fileName)
                relative_path = os.path.relpath(local_Path , file_from)
                dropBox_path = os.path.relpath(file_to , relative_path)
                with open(local_Path , 'rb')as f :
                    dbx.files_upload(f.read(),dropBox_path, mode = WriteMode('overwrite'))
def main():
    access_token = 'sl.A-tZbWVkgBEMKsckI411nqaB4exXAxKP48AQRoKwl7D3Q6wE0uUNRruIsU9qb5YSBW5YddP5zJnmqQEZzH7tPvKTwIwFe3ht8v7VKRoVovPU3uVl7LbL6aNmCZWHhR9nnb_B8Xw'
    transferData = TransferData(access_token)
    file_from = str(input(f"Enter the folder path to transfer :"))
    file_to = str(input(f"Enter the full path to upload :"))
    transferData.upload_file(file_from , file_to)
    print("File has been moved")
main()

