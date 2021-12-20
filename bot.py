import requests

from constants import id, pw

s = requests.Session()

def login_deu():
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
