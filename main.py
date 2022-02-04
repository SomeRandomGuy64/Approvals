import shutil, os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
#countFile = 0

#initializes an empty array
fileList = list()

#split extension and filename
def fileName(x):
    fn = os.path.splitext(x)[0]
    return fn

def extension(x):
    e = os.path.splitext(x)[1]
    return e

#code to choose a directory
currdir = os.getcwd()

target = filedialog.askdirectory(parent=root, initialdir=currdir, title="Please select a directory")

originalFile = 0
for path in os.listdir(target):
    #looks for an approval
    if fileName(path).endswith("A"):
        #sets the approval as the original file
        originalFile = path
        #saves the extension of the original file
        newExtension = extension(originalFile)
   #elif fileName(path) = ''
   #    print("No filepath has been selected")
    else:
        #if the file isn't the approval the filename gets added to an array
        fileList.append(fileName(path))
    #prints the name of each file in the target directory
    #print(path)
    #if os.path.isfile(os.path.join(target, path)):
    #    countFile += 1

#iterator for the array
fileListNo = 0
#checks that there is an original file
if originalFile != 0:
    #for loop to do the copying
    for x in fileList:
        #gets the file name from the current position of the array
        newFilename = fileList[fileListNo]
        #makes sure the current file doesn't already have an approval
        if (newFilename + "A") != fileName(originalFile):
            #sets the original file directory
            originalFileDirectory = str(target + "/" + originalFile)
            #sets the new file directory
            newFile = str(target + "/" + newFilename + "A" + newExtension)
            #copies and pastes the file
            shutil.copyfile(originalFileDirectory, newFile)
        #iterates so the next item in the array can be accessed
        fileListNo += 1
else:
    print("There isn't an approval")
    #input('Press ENTER to exit')
