import os
import sys

chang = 0
changCun = 0

def tab():
    global chang
    global changCun
    while chang >= 1:
        run.write("\t")
        chang -= 1
    chang = changCun
def addTab():
    global chang
    global changCun
    chang += 1
    changCun += 1
def faukTab():
    global chang
    global changCun
    chang -= 1
    changCun -= 1

filenameAll = sys.argv[2]
filename = sys.argv[2].split(".")[0]

run = open(f"{filename}.java","w+",encoding="utf-8")
run.write(f"public class {filename}" + "{\n")
addTab()
run.close()
run = open(f"{filename}.java","a",encoding="utf-8")

if sys.argv[1] == "run":
    
    # 使用with语句打开文件，确保文件最终会被关闭
    with open(filenameAll, 'r', encoding='utf-8') as file:
        # 逐行读取文件
        for line in file:
            # 处理每一行，例如打印出来
            print(line.strip())  # strip()用于去除每行末尾的换行符
            x = line.split(" ")
            if x[0] == "import":
                if x[1] == "<oil>":
                    kuName = x[2].strip()
                    run.write(open(f"{os.environ.get('APPDATA')}\\oil_lang\\{kuName}.oil").read())
            else:
                run.write(f"\t{line}")
        run.write("\n}")
        run.close()