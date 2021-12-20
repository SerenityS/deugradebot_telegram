import requests

from constants import id, pw

s = requests.Session()

def login_deu():
    app_login_url = "https://smartdeu.deu.ac.kr/applogin.do"
    login_data = {'user_id': id, 'passwd': pw}

    login_result = s.post(app_login_url, json=login_data)

    if login_result.json()['SUCCESS_YN'] == "Y":
        print("로그인 성공")
    else:
        print("로그인 실패")
        raise Exception("LoginInfoMismatch")


if __name__ == "__main__":
    login_deu()
