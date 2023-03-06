import os

path="/Users/tumbler/Documents/Coding/pp2/git/TSIS6"
delete_path ="/Users/tumbler/Documents/Coding/pp2/git/TSIS6/delete_file"
# 1
print(os.listdir(path))
# 3
if os.path.exists(path):
    print(os.path.splitext(os.path.basename(path))[0])
    print(os.listdir(path))
# 2
print(os.access(path,os.F_OK))
print(os.access(path,os.R_OK))
print(os.access(path,os.W_OK))
print(os.access(path,os.X_OK))
# 4
print(len(open("for_test/text.txt","r").readlines()))

# 6
for i in range(65,91):
    test=f"for_test/"+chr(i)+".txt"
    with open(test,"w") as f:
        # os.remove(test)
        f.close()

# 7
def copy(text,file_):
    txt = open(text,"r")
    coping_txt = open(file_,"w")

    coping_txt.write(txt.read())

copy("for_test/text.txt","for_test/copied_text.txt")

# 8
if os.path.exists(delete_path) and os.access(path,os.R_OK and os.W_OK and os.R_OK):
    os.remove(delete_path)
# else:
#     open("delete_file","w")

