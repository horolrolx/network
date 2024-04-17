import os
def get_file_list_1():
    file_list = [file for file in os.listdir("./computer_network/") if '.md' in file]
    file_list = sorted(file_list)
    return file_list
  
def make_info_1(file_list):
    info = f"## 컴퓨터 네트워크 공부 정리\n\n"
    for file in file_list:
        temp = f"- [{file}](https://github.com/xoxlo/network/tree/main/computer_network/{file})\n"
        info += temp
    return info

def get_file_list_2():
    file_list = [file for file in os.listdir("./network_specialism/") if '.md' in file]
    file_list = sorted(file_list)
    return file_list
  
def make_info_2(file_list):
    info = f"## 네트워크 특론 정리\n\n"
    for file in file_list:
        temp = f"- [{file}](https://github.com/xoxlo/network/tree/main/network_specialism/{file})\n"
        info += temp
    return info

def get_file_list_3():
    file_list = [file for file in os.listdir("./computer_network/중간고사 예상 문제/") if '.md' in file]
    file_list = sorted(file_list)
    return file_list
  
def make_info_3(file_list):
    info = f"## 컴퓨터 네트워크 중간고사 예상 문제\n\n"
    for file in file_list:
        temp = f"- [{file}](https://github.com/xoxlo/network/tree/main/computer_network/중간고사 예상 문제/{file})\n"
        info += temp
    return info

def get_file_list_4():
    file_list = [file for file in os.listdir("./computer_specialism/중간고사 예상 문제/") if '.md' in file]
    file_list = sorted(file_list)
    return file_list
  
def make_info_4(file_list):
    info = f"## 네트워크 특론 중간고사 예상 문제\n\n"
    for file in file_list:
            temp = f"- [{file}](https://github.com/xoxlo/network/tree/main/network_specialism/중간고사 예상 문제/{file})\n"
        info += temp
    return info
  
def make_read_me(info):
    return f"""
    
# 컴퓨터 네트워크
# 네트워크 특론
정리

{info}
"""


def update_readme():
    file_list1 = get_file_list_1()
    file_list2 = get_file_list_2()
    file_list3 = get_file_list_3()
    file_list4 = get_file_list_4()
    info = make_info_1(file_list1) + make_info_2(file_list2) + make_info_3(file_list3) + make_info_4(file_list4)
    readme = make_read_me(info)
    return readme


if __name__ == "__main__":
    readme = update_readme()
    with open("./README.md", 'w', encoding='utf-8') as f:
        f.write(readme)
