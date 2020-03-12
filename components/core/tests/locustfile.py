from locust import HttpLocust, TaskSequence, task, seq_task, between

class UserBehavior(TaskSequence):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    def on_start(self):
        self.login()

    def login(self):
        res = self.client.post("/api/login", "user_name=rand&password=pass", headers=self.headers)
        self.headers['token'] = res.headers['token']

    @seq_task(1)
    @task(1)
    def user_requests(self):
        self.client.get("/api/user/requests", headers=self.headers)

    @seq_task(2)
    @task(1)
    def user_blocked(self):
        self.client.get("/api/user/blocked", headers=self.headers)

    @seq_task(3)
    @task(3)
    def user_downloads(self):
        downloadEndpoints = [25, 50, 75]
        for endpoint in downloadEndpoints:
            self.client.get("/api/user/downloads/" + str(endpoint), headers=self.headers)

    @seq_task(4)
    @task(2)
    def get_downloads_request(self):
        requestEndpoints = [25, 50, 75]
        for endpoint in requestEndpoints:
            self.client.get("/api/downloads/" + str(endpoint), headers=self.headers)

    @seq_task(5)
    @task(3)
    def get_user_heavy(self):
        self.client.get("/api/user/heavy", headers=self.headers)

class APIUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(1, 15)