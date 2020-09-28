#!/user/bin/python
# _*_ coding:utf-8 _*_
import requests

__author__ = "super.gyk"


#  python post请求上传文件
class UploadFile(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/78.0.3904.108 Mobile Safari/537.36',
        }
        self.url = 'http://xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        self.token = 'YCDCJVKVK2dJDCM0WI9FMYCVI8dJJYVI:SrWB6NBg1zNsuapd2oI-j7alJnA=:eyJzY29wZSI6ImVoaXMtcmVjb3JkZXItZG16' \
                     'LXN0ZyIsImRlYWRsaW5lIjoxNjAxMjc0NDMyfQ=='

    def send_file(self):
        file_data = {
            'file': open('one.png', 'rb')
        }
        form_data = {
            'token': self.token
        }
        req = requests.post(self.url, data=form_data, files=file_data, headers=self.headers)
        print(req.text)


if __name__ == '__main__':
    up_file = UploadFile()
    up_file.send_file()
