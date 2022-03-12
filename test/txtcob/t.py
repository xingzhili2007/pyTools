path1 = "./test/txtcob/1.txt"
path2 = "./test/txtcob/2.txt"
path3 = "./test/txtcob/3.txt"

file1 = open(path1, "r", encoding="utf-8", errors="ignore")
file2 = open(path2, "r", encoding="utf-8", errors="ignore")
file3 = open(path3, "w", encoding="utf-8", errors="ignore")

while True:
    mystr1 = file1.readline()  #表示一次读取一行
    mystr2 = file2.readline()
    if not mystr1:
        #读到数据最后跳出，结束循环。数据的最后也就是读不到数据了，mystr为空的时候
        break
    #print(mystr,end="")#打印每次读到的内容
    file3.write(mystr1[:-1])
    file3.write("    ")
    file3.write(mystr2)

file1.close()
file3.close()
