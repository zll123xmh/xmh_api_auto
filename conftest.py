import pytest
from common.resquest_util import http
@pytest.fixture(scope="session")
def get_token():
    # 登录获取token，整个测试会话只执行一次
    login_data = {
        "username": http.cfg["test_user"]["username"],
        "password": http.cfg["test_user"]["password"]
    }
    resp = http.send("post", "/api/login", json_data=login_data)
    token = resp.json()["data"]["token"]
    yield token
    # 后置：登出操作
    http.send("post", "/api/logout", headers={"token":token})
