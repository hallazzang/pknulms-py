import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class LMSClient:
    def __init__(self):
        self.session = requests.Session()

    def login(self, id, pw):
        url = 'https://lms.pknu.ac.kr/ilos/lo/login.acl'
        headers = {
            'Referer': 'http://lms.pknu.ac.kr/ilos/main/member/login_form.acl',
        }
        data = {
            'returnURL': '',
            'challenge': '',
            'response': '',
            'usr_id': id,
            'usr_pwd': pw,
        }
        r = self.session.post(url, headers=headers, data=data, verify=False)

        return '로그인 정보가 일치하지 않습니다' not in r.text


if __name__ == '__main__':
    lms = LMSClient()
    print(lms.login('XXX', 'XXX'))
