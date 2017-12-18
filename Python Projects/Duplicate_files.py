
#Open both files, read in data.
#compare data, if same delete second instance

import os

list_of_files = os.listdir('.')
dictionary_of_read_files = {}
duplicates = []
list_of_files.sort()
print(list_of_files)
for i in list_of_files:
    newFile = open(os.path.join('.', i))
    dictionary_of_read_files[i] = newFile.read()
    newFile.close()

for i in range(0 , len(list_of_files)):
    for y in range(i+1, len(list_of_files)):
        #print("Comparing " + i + "to " + y )
        if dictionary_of_read_files[list_of_files[i]] == dictionary_of_read_files[list_of_files[y]]:
            #print("\n" + y +"is a duplicate. Preparing to delete!")
            if list_of_files[y] in duplicates:
                continue
            else:
                duplicates.append(list_of_files[y])



for i in duplicates:
    print(duplicates)
    print("Removing " + i)
    os.remove(i)
