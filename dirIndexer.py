import os
import re

output = ''
i = 0

print('Welcome to directory indexer.')

while(True):
    sourceDir = str(input('Enter a directory to index > '))
    if os.path.exists(sourceDir):
        break
    else:
        print('Directory does not exist. Please enter a valid directory.')


outputFileName = 'fileindex'
outputFileExt = '.txt'
outputFilePath = os.path.join(sourceDir, outputFileName + outputFileExt)

if os.path.exists(outputFilePath):
    choice = str(input('file already exists. override? (y/n/enter) > '))
    if choice == 'y' or len(choice) == 0:
        print('overriding file')
        os.remove(outputFilePath)
    else:
        print('exiting...')
        exit()

outputFile = open(outputFilePath, 'w')
dirContents = os.listdir(sourceDir)

indexDecision = str(
    input('What to index? (f)iles, (d)irectories or (e)verything? (efd) > '))

if(len(indexDecision) == 1):
    indexDecision = indexDecision.lower()
    regexResult = re.match('[fed]', indexDecision)
    if regexResult != None:
        # valid input
        print('choice: ' + indexDecision)
    else:
        print('Invalid input, defaulting to everything')
        indexDecision = 'e'
else:
    print('Invalid input, please enter only one letter; f , d OR e. Defaulting to everything')
    indexDecision = 'e'


# if(indexDecision.find('f') != -1 & indexDecision.find('d') != -1 & indexDecision.find('e') != -1):
#     print('Invalid input, defaulting to everything fde')
#     indexDecision = 'e'
# elif(indexDecision.find('f') != -1 & indexDecision.find('d') != -1):
#     print('Invalid input, defaulting to everything fd')
#     indexDecision = 'e'
# elif(indexDecision.find('f') != -1 & indexDecision.find('e') != -1):
#     print('Invalid input, defaulting to everything fe')
#     indexDecision = 'e'
# elif(indexDecision.find('f') == -1 & indexDecision.find('d') == -1 & indexDecision.find('e') == -1):
#     print('Invalid input, defaulting to everything no fde')
#     indexDecision = 'e'


if(indexDecision.find('d') != -1 or indexDecision.find('e') != -1):
    for dirName in dirContents:
        if os.path.isdir(os.path.join(sourceDir, dirName)):
            output = output + f'{dirName}/\n'
            i = i + 1

if(indexDecision.find('f') != -1) or (indexDecision.find('e') != -1):
    for fileName in dirContents:
        if os.path.isfile(os.path.join(sourceDir, fileName)):
            if(fileName != outputFileName + outputFileExt):
                output = output + f'{fileName}\n'
                i = i + 1

output = output.strip()

print(output, file=outputFile)
if(indexDecision.find('e') != -1):
    print(f'{i} files & directories indexed. Output file: {outputFileName + outputFileExt}')
elif(indexDecision.find('f') != -1):
    print(f'{i} files indexed. Output file: {outputFileName + outputFileExt}')
elif(indexDecision.find('d') != -1):
    print(f'{i} directories indexed. Output file: {outputFileName + outputFileExt}')

#print(f'Successfully created index file for {str(i)} files. Output file: {outputFileName + outputFileExt}')
