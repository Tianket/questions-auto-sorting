import os
import platform

answers = {}
choices = []
judge = "<h3 class=\"mark_name colorDeep\">"
check = "check_answer"
choice = "num_option"

if (platform.system() == 'Windows'):
    path = ".\\"
else:
    path = "./"


def file_name(file_dir=path):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == ('.html'):
                L.append(file)
    return L


print("请选择正确答案和你的答案：\n")

for i in range(len(file_name())):
    print("{}:{}".format(i + 1, file_name()[i]))

print("\n")
choiceee = int(input("正确答案的那个文件："))
his_answer = file_name()[choiceee - 1]
choiceee = int(input("你的答案的那个文件："))
my_answer = file_name()[choiceee - 1]

bool = False
title = ""

file = open(os.path.join(path, "answer.txt"), 'w', encoding="utf-8")

with open(os.path.join(path, his_answer), 'r', encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if check in line:
            # next line is true answer
            bool = True
            continue

        if bool:
            # this answer is true, split it
            answers[title] = line[line.find("<p>")+2:line.find("</p></div>")]
            file.write(line[line.find("<p>")+2:line.find("</p></div>")] + "\n")
            bool = False

        if line[:len(judge)] == judge:
            # this is a question
            file.write("\n" + line[len(judge)] + "\n")
            title = line[line.find("ow:hidden;\">") + 12:]
            title = title.strip("</div></h3>")
            title = title.strip("</p>")
            title = title.strip("<br")
            file.write(title + "\n")
file.close()
print("\n答案已保存至当前目录\n")

this_answer = "瞎写的程序别来打我啊"

with open(os.path.join(path, my_answer), 'r', encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if judge in line:
            # this is a question
            title = line[line.find("ow:hidden;\">") + 12:]
            title = title.strip("</div></h3>")
            title = title.strip("</p>")
            title = title.strip("<br")
            this_answer = answers[title]

        if choice in line:
            # next line is a choice
            this_one = line[line.find("\">") + 2:line.find("</span>", line.find("\">"))]

        if "fl answer" in line and (line[line.find("<p>")+2:line.find("</p></div>")]) == this_answer:
            choices.append(this_one)
print("属于你的答案：")
for i in range(len(choices)):
    if (i + 1) / 5 == 0:
        print("\n")
    print(choices[i], end="")

if path == ".\\":
    print("\n")
    os.system("pause")
