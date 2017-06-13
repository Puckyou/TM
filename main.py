import glob
import os
import csv
import re

def get_encoding(file):
    import chardet
    with open(file, "rb") as f:
        data = f.read()
        file_encoding = chardet.detect(data)["encoding"]
    return file_encoding

files = glob.glob(os.path.join("Texts", "*.txt"))
my_dict = {}
all_lines = []
sum_count = 0
for file in files:
    with open(file, "r", encoding = get_encoding(file)) as f:
       for line in f:
           line_2 = f.readline()
           cyril1 = re.findall(u"[\u0400-\u0500]+", line)
           cyril2 = re.findall(u"[\u0400-\u0500]+", line_2)
           if cyril1 != [] and cyril2 != []:
               sum_count += 1
               new_list = [line, line_2]
               new_line = " ".join(new_list)
               all_lines.append(new_line)
           else:
               all_lines.append(line)
               all_lines.append(line_2)
while sum_count != 0:
    new_lines = []
    for i, line in enumerate(all_lines):
        sum_count = 0
        if i == len(all_lines)-1:
            break
        else:
            line_2 = all_lines[i+1]
            cyril1 = re.findall(u"[\u0400-\u0500]+", line)
            cyril2 = re.findall(u"[\u0400-\u0500]+", line_2)
            if cyril1 != [] and cyril2 != []:
                sum_count += 1
                new_list = [line, line_2]
                new_line = " ".join(new_list)
                new_lines.append(new_line)
            else:
                new_lines.append(line)
                new_lines.append(line_2)
    all_lines = new_lines
new_list = []
my_dict = dict(all_lines [i:i+2] for i in range(0, len(all_lines), 2))
new_dict = {}
for key, values in my_dict.items():
    new_dict["RU"] = key
    new_dict["CH"] = values
print(my_dict)
with open('mycsvfile.csv', 'w', encoding="UTF-8") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ', dialect="excel")
    for lines in my_dict.items():
        spamwriter.writerows([lines])
