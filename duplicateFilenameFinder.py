import os

# getFilePathsRecursively gets the location of any file in any subdirectory and returns a list of filepaths relative to rootdir
def getFilePathsRecursively(directory):
    files = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(dirpath, filename))
    return files

# determineDuplicateFilenames takes a list of filepaths, extracts the filenames (without extension) and in a case-insensitive way remembers filename duplicates.
# This function returns a dict where the duplicate filename is the key and the value is a list consisting of each full filepath that contains that filename. 
def determineDuplicateFilenames(fileList):
    # dict where key is filename and value is list of full filepaths
    duplicateFiles = {}

    for fullFilePath in fileList:
        # extract filename from filepath
        fileNameWithType = os.path.basename(fullFilePath)
        fileNameWithoutType, _ = os.path.splitext(fileNameWithType)
        fileNameWithoutTypeLowercase = fileNameWithoutType.lower() # case insensitive matching
        
        # check whether this key already exists in dict
        if fileNameWithoutTypeLowercase in duplicateFiles:
            # append it to list
            duplicateFiles[fileNameWithoutTypeLowercase].append(fullFilePath)
        else:
            # create value which is list that only has one item now
            duplicateFiles[fileNameWithoutTypeLowercase] = [fullFilePath]

    # remove all trivial duplicates (a single occurance)
    actualDuplicateFiles = {key: value for key, value in duplicateFiles.items() if len(value) > 1}

    return actualDuplicateFiles

def main():
    rootdir = "."
    fileList = getFilePathsRecursively(rootdir)
    duplicateFileLocations = determineDuplicateFilenames(fileList)

    # print result in readable way
    for k, v in zip(duplicateFileLocations.keys(), duplicateFileLocations.values()):
        print(f"{k} is a duplicate file with {len(v)} occurances:")
        for occ in v:
            print("\t", occ)
        print()

    print(f"----\nSummary: Found a total of {len(duplicateFileLocations)} files that had duplicates.")

main()
