#Function.py
import tarfile

def Untar(filePath):
    tar = tarfile.open(filePath)
    tar.extractall()
    tar.close()
