import allure
from common.resquest_util import http

@allure.feature("登录模块")
class TestLogin:

    @allure.story("正常登录")
    def test_login_success(self):
        data = {
            "username": http.cfg["test_user"]["username"],
            "password": http.cfg["test_user"]["password"]
        }
        resp = http.send("post", "/api/login", json_data=data)
        assert resp.status_code == 200
        assert resp.json()["code"] == 200

    @allure.story("密码错误登录")
    def test_login_pwd_error(self):
        data = {
            "username": http.cfg["test_user"]["username"],
            "password": "666666"
        }
        resp = http.send("post", "/api/login", json_data=data)
        assert resp.json()["code"] == 400
