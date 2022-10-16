
import os
import time

from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

class Auther:

    def __init__(self,
            username:str,password:str,
            edge_driver = "./msedgedriver.exe",
            check_interval = 1,
            ping_ip = "114.114.114.114",
        ) -> None:

        self.edge_driver = edge_driver
        os.environ["webdriver.edge.driver"] = edge_driver

        self.username = username
        self.password = password
        self.ping_ip = ping_ip
        self.sleep_time = check_interval
    def is_connected(self):
        return os.system("ping %s"%(self.ping_ip)) == 0

    def login(self):
        edge_service_args = Options()
        edge_service_args.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Edge(service_args=edge_service_args)
        driver.get("http://10.0.0.55")
        
        username_input = driver.find_element(by=By.ID,value = "username")
        username_input.send_keys(self.username)

        password_input = driver.find_element(by=By.ID,value="password")
        password_input.send_keys(self.password)

        login_button = driver.find_element(by=By.ID,value="login")
        login_button.click()

        driver.close()

    def start(self):
        while True:
            if self.is_connected():
                print("网络已连接.")
            else:
                print("尝试登录网络.")
                self.login()
            time.sleep(self.sleep_time)

if __name__=="__main__":
    auther = Auther("学号","密码")
    auther.start()