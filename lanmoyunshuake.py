import requests
import re
import time

class shua(object):
    def __init__(self, username, password):
        self.login_url = "https://www.mosoteach.cn/web/index.php?c=passport&m=account_login"
        self.watchUrl = "https://www.mosoteach.cn/web/index.php?c=res&m=save_watch_to"
        self.username = username
        self.password = password
        self.r_id = []
        self.info = []
        self.s = requests.Session()


    def login(self):
        data = {
            "account_name": self.username,
            "user_pwd":  self.password,
            "remember_me": "N"
        }
        self.s.post(url=self.login_url, data=data)


    def watchClass(self):
        url = "https://www.mosoteach.cn/web/index.php?c=res&m=index&clazz_course_id=3EEA316A-D4E1-11E7-AA22-7CD30AD36C02"
        header = {
            "cookie": "login_token=16275400247fd049140be2e59499059fd0e2368baf8cf40c35f4eb5d0cf2b353; mosoteach2=998589c0429e418a258086ed7937da6d8d284b7b; SERVERID=f0604134d61da9c8ecf31e28d9bb4135|1512577524|1512577253"
        }
        r = requests.get(url, headers=header)
        res_ids = re.findall("data-value=\"(.*?)\"", r.text, re.S)
        for res_id in res_ids:
            self.r_id.append(res_id)
        i = 1
        while(i<=36):
            data = {
                "clazz_course_id": "3EEA316A-D4E1-11E7-AA22-7CD30AD36C02",
                "res_id": self.r_id[i],
                "watch_to": "2000",
                "duration": "2000",
                "current_watch_to": "0"
            }
            r = self.s.post(url=self.watchUrl, data=data)
            print r.text
            i+=1
            time.sleep(5)


hd = shua("用户名", "密码")
hd.login()
hd.watchClass()