import os

dir = os.getcwd()
txt_dir = 'Sorting'
dir_path = os.path.join(dir, txt_dir)
merge = []

for filename in os.listdir(dir_path):
    with open(os.path.join(dir_path, filename), 'r', encoding='utf-8') as f:
        text = f.readlines()
        len_ = len(text)
        merge.append((filename, len_, text)) 

def get_len_text(file_len): 
    return file_len[1]   

merge.sort(key=get_len_text) 

with open(os.path.join(dir, 'mix.txt'), 'w', encoding='utf-8') as outfile:
    for filename, len_, text in merge:
        outfile.write(str(filename) + "\n")
        outfile.write(str(len_) + "\n")
        outfile.writelines(text) 
        outfile.write("\n")