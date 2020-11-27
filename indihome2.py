from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary




post_data = {
                'UserName': 'Support',
                'PassWord': 'sdafdsafdff',#base64.b64encode('theworldinyourhand'),
            }

header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.83 Mobile Safari/537.36',
    'Referer': 'http://10.88.216.6:80/',
    'Cookie': 'Cookie=body:Language:english:id=-1',
}


def brute():
    session = requests.Session()
    post_data,header=persiapan()

    hasil= session.post('https://10.88.216.6:80/login.cgi',post_data,headers=header,timeout=5,verify=False)
    #print (hasil.content)
    print (hasil.url)


if __name__ == "__main__":
    print('''
        ''')
    print('''Author : none_knows
Version : 0.1b''')                                                                                                   
    '''opts = Options()
    opts.add_argument('--allow-running-insecure-content')
    opts.add_argument('--ignore-certificate-errors')
    # opts.set_headless()
    #opts.headless = True
    #assert opts.headless  # Operating in headless mode
    #capabilities = webdriver.DesiredCapabilities().FIREFOX
    #capabilities['acceptSslCerts'] = True

    browser = Firefox(options=opts)
    browser.get("https://10.88.216.6:80")
    #print(browser.page_source.encode("utf-8"))
    #browser.find_element_by_id('advancedButton').click()
    #browser.get("https://duckduckgo.com")
    #print(browser.page_source.encode("utf-8"))'''

	caps = DesiredCapabilities.FIREFOX.copy()
	caps ['acceptInsecureCerts'] = True
	ff_binary=FirefoxBinary('path to the Nightly binary')
	driver=webdriver.Firefox(firefox_binary=ff_binary, capabilities=caps)
	driver.get("http://10.88.216.6:80")

    username = browser.find_element_by_id('txt_Username').send_keys('Support')
    password = browser.find_element_by_id('txt_Password').send_keys('theworldinyourhand')
    browser.find_element_by_id('button').click()
    #browser.get("https://10.88.216.6:80/frame.asp")
    browser.find_element_by_xpath("//div[@name='maindiv_WlanBasic']").click()
    browser.find_element_by_xpath("//div[@name='subdiv_WlanBasic']").click()
    #print(browser.page_source.encode("utf-8"))    
