# import requests,json
# class SendMethod:
#     def send_method(self,url=None,method=None,header=None,data=None,params=None):
#         if method == "POST":
#             response = requests.post(url=url,data=data)
#         elif method == "GET":
#             response = requests.get(url=url,params=params)
#         else:
#             response = None
#         result = {}
#         if response is not None:
#             result["body"] = response.text
#             result["status_code"] = response.status_code
#             return result
#         else:
#             return None
# if __name__ == '__main__':
#     url = "https://www.baidu.com"
#     method = "POST"
#     header = {
#         "Content-Type": "application/json",
#         "Authorization": "Bearer {token}"
#     }
#     data = {
#
#     }
# result = SendMethod().send_method(url=url,method=url)
# new_result = json.dumps(result,ensure_ascii=False,indent=4)
# print(result)

import requests
import yaml

class HttpRequest:
    def __init__(self):
        # 读取配置
        with open("config/config.yaml", encoding="utf-8") as f:
            self.cfg = yaml.safe_load(f)
        self.base_url = self.cfg["base_url"]
        self.session = requests.Session() # session自动保持cookie

    def send(self, method, path, json_data=None, params=None, headers=None):
        url = self.base_url + path
        res = self.session.request(
            method=method,
            url=url,
            json=json_data,
            params=params,
            headers=headers
        )
        return res

# 全局实例，用例直接调用
http = HttpRequest()
