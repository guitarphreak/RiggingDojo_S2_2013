import os


def findAllFiles(fileDirectory, fileExtension):
    # Return a list of all file names, excluding the file extension
    allFiles = os.listdir(fileDirectory)
     
    # Refine all files, listing only those of the specified file extension
    returnFiles = []
    for f in allFiles:
        splitString = str(f).rpartition(fileExtension)
        if not splitString[1] == "" and splitString[2] == "" and splitString[0] != '__init__':
            returnFiles.append(splitString[0])
 
    return returnFiles