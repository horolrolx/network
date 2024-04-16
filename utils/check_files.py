import os
def get_file_list_prac():
    file_list = [file for file in os.listdir("./공부정리/") if '.md' in file]
    file_list = sorted(file_list)
    return file_list
  
def make_info_prac(file_list):
    info = f"## 공부 정리\n\n"
    for file in file_list:
        temp = f"- [{file}](https://github.com/xoxlo/computer_network/tree/main/공부정리/{file})\n"
        info += temp
    return info
  
def make_read_me(info):
    return f"""
    
# 컴퓨터 네트워크1

정리

{info}
"""


def update_readme():
    file_list_prac = get_file_list_prac()
    info = make_info_prac(file_list_prac)
    readme = make_read_me(info)
    return readme


if __name__ == "__main__":
    readme = update_readme()
    with open("./README.md", 'w', encoding='utf-8') as f:
        f.write(readme)
