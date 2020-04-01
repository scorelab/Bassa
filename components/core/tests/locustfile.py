# for use with the Locust framework
# https://locust.io/

from locust import HttpLocust, TaskSet, task, between
from random import randint

USERNAME = "rand"
PASSWORD = "pass"
SERVER_SECRET_KEY = "123456789"

class UserBehavior(TaskSet):
    headers = {
        'Host': 'localhost:5000',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://localhost:3000',
    }

    def on_start(self):
        res = self.client.post("/api/login", "user_name={}&password={}".format(USERNAME, PASSWORD), headers=self.headers)
        self.headers['token'] = res.headers['token']

    @task(1)
    def get_user_signup_requests(self):
        self.client.get("/api/user/requests", headers=self.headers)

    @task(1)
    def get_blocked_users_request(self):
        self.client.get("/api/user/blocked", headers=self.headers)

    @task(1)
    def get_downloads_user_request(self):
        self.client.get("/api/user/downloads/" + str([50, 100, 150][randint(0, 2)]), headers=self.headers)

class APIUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(2, 7)
