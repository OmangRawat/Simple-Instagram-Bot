from selenium import webdriver
from time import sleep


class IBot:
    def __init__(self, un, pw):
        self.driver = webdriver.Chrome()
        self.un = un
        self.pw = pw
        self.driver.get("http://instagram.com")
        sleep(2)
        # self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article'
        #                                   '/div[2]/div[1]/div/form/div/div[1]/div').send_keys(un)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form'
                                          '/div/div[1]/div/label/input').send_keys(un)              # Enter Username
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form'
                                          '/div/div[2]/div/label/input').send_keys(pw)              # Enter Password
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article'
                                          '/div[2]/div[1]/div/form/div/div[3]/button/div').click()  # Click Login
        sleep(4)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
        sleep(4)                                                                                    # Click Not Now
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        sleep(4)                                                                                    # Click Not Now
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[1]'
                                          '/div/div/div[2]/div[1]/div/div/a').click()               # Click on username
        sleep(2)

    def get_following(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header'
                                          '/section/ul/li[3]/a').click()                            # Click on following
        # sug = self.driver.find_element_by_xpath('')
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")          # Take all Username
        prev, current = 0, 1
        while prev != current:
            prev = current
            sleep(1)
            current = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;""", scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')                                           # Scroll Down
        names = [name.text for name in links if name.text != '']
        print("\nFOLLOWING :")
        print(len(names))
        print(names)
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div'                    # Click on cross
                                          '/div[2]/button').click()
        sleep(2)
        return names

    def get_followers(self):
        """self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/'
                                          'div[3]/div[1]/div/div[2]/div[1]/a').click()
        sleep(10)"""
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header'               # Click on Followers
                                          '/section/ul/li[2]/a').click()
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")          # Take all Username
        prev, current = 0, 1
        while prev != current:
            prev = current
            sleep(1)
            current = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;""", scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')                                           # Scroll Down
        names = [name.text for name in links if name.text != '']
        print("\nFOLLOWERS :")
        print(len(names))
        print(names)
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div'                               # Click on cross
                                          '/div[1]/div/div[2]/button').click()
        return names

    def logout(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header'               # Click Options
                                          '/section/div[1]/div/button').click()
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/button[9]').click()    # Click Logout

    def get_nf(self):
        sleep(10)
        following = self.get_following()
        followers = self.get_followers()
        nf = []
        for name in following:
            if name not in followers:
                nf.append(name)
        print("\nNOT FOLLOWING YOU :")
        print(len(nf))
        print(nf)
        self.logout()


print("****Requirements****")
print("****You should have an Instagram Account****")
print("****This program runs using Google Chrome so ensure Chrome is downloaded on your System****")
print("****Check if your Chrome Driver version is same as the Chrome Browser you are using"
      " before we start Automated Data Fetching****")
print("If you have the requirements fulfilled enter 1")
print("Else enter 0")
start = input()
if start == "1":
    print("Enter Your Username")
    username = str(input())
    print("Enter Your Password")
    password = str(input())
    print("\n")
    profile = IBot(username, password)
    profile.get_nf()
else:
    print("Download the required Chrome Driver from https://chromedriver.chromium.org/downloads and"
          " shift it to the same folder as the program")
