import os
fileName = "" + ".txt"
folder_path = os.path.join("Diaries", fileName)


for root, dirs, files in os.walk(folder_path):
    print("hello")

for root, dirs, files in os.walk("Diaries"):
    for file_name in files:
        current_file_path = os.path.join(root, file_name)
        print(current_file_path)
        print(root)
        print(dirs)
        print(files)
        current_diary = open(current_file_path, "w")
        current_diary.write("GET WREKT SKRUB")
        current_diary.close()


# replace their text with the phrase "GET WREKT SKRUB!"
print("------")
