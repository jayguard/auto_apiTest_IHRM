import requests


class DepartmentApi:
    def __init__(self):
        self.dep_url = "http://182.92.81.159/api/company/department"

    def add_dep(self, name, code, headers):
        jsonData = {
            "name": name,
            "code": code,
            "manager": "咸鱼",
            "introduce": "这是个与众不同的咸鱼",
            "pid": ""
        }
        return requests.post(self.dep_url, json=jsonData, headers=headers)

    def query_dep(self, id, headers):
        query_dep_url = self.dep_url + "/" + id
        return requests.get(query_dep_url, headers=headers)

    def modify_dep(self, id, headers, name, code, manager=None, introduce=None):
        modify_dep_url = self.dep_url + "/" + id
        return requests.put(modify_dep_url, headers=headers, json={"name":name, "code":code, "manager":manager, "introduce":introduce})

    def delete_dep(self, id, headers):
        delete_dep_url = self.dep_url + "/" + id
        return requests.delete(delete_dep_url, headers=headers)


