import requests

from bs4 import BeautifulSoup
from constants import id, pw

s = requests.Session()


def get_grade_data():
    grade_list = []

    grade_data_url = "https://smartdeu.deu.ac.kr/viewProcess/stud/d/DM01_D001.do"

    grade_data_header = {'Accept': "*/*"}
    grade_data_param = {'year': "2021", 'smt': "20", 'menuCd': "300023", 'spNm': ["Up_App_Usb0301q_Check", "Up_App_Usb0301q"]}

    grade_data_html = s.get(grade_data_url, headers=grade_data_header, params=grade_data_param)
    grade_data_parsed = BeautifulSoup(grade_data_html.text, 'html.parser')
    grade_data_parsed = grade_data_parsed.find_all(class_="detail_info column2 dw50")
    for grade_data in grade_data_parsed:
        gd = grade_data.find_all("dd")
        grade_list.append({'lectureName': gd[2].text, 'profName': gd[4].text, 'score': gd[6].text, 'grade': gd[7].text})

    return grade_list


def login_deu_app():
    app_login_url = "https://smartdeu.deu.ac.kr/applogin.do"
    login_data = {'user_id': id, 'passwd': pw}

    login_result = s.post(app_login_url, json=login_data)

    if login_result.json()['SUCCESS_YN'] == "Y":
        login_deu_web()
        print("로그인 성공")
    else:
        print("로그인 실패")
        raise Exception("LoginInfoMismatch")


def login_deu_web():
    web_login_url = "https://smartdeu.deu.ac.kr/weblogin.do"
    login_data = {'user_id': id, 'passwd': pw}

    s.post(web_login_url, data=login_data)


if __name__ == "__main__":
    login_deu_app()
