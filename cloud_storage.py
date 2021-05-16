import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f=open (file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main ():
    access_token='b2qNFhCurF0AAAAAAAAAAf8hJoR4M_JwjgJeMpGTQFyRguyGQEut5YrIzr_jPtWC'        
    transferData=TransferData(access_token)

    file_from=input("Enter the file path to transfer : ")
    file_to=input('Enter the full path to upload to dropbox : ')

    transferData.upload_file(file_from,file_to)
    print("the file is uploaded successfully")

main()    