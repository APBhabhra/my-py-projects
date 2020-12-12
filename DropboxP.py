import dropbox
class Transferdata:
    def __init__(self,accesstoken):
        self.access_token=accesstoken
    def Uploadfiles(self,filefrom,fileto):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(filefrom,"rb")
        dbx.files_upload(f.read(),fileto)
def maim():
    a="sl.AmcbmaXz66kA1dce3MvO4i87G_nId4-9ea8-JfFXlzmHJcuI65SNxLqUqxofzfFvaLc4y4pqiKY0lbC4Yq15csYQR3XQL9SWs-TJWcDwrTgJHIWddJpq-DInxMcWTw697DCWqWsHbHg"
    p=Transferdata(a)
    filefrom=(input("Enter the source path"))
    fileto=(input("Enter the destination path"))
    p.Uploadfiles(filefrom,fileto)
    print("File has been uploaded")
maim()
