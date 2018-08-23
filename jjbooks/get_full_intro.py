import selenium.webdriver as webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://wap.jjwxc.net/book2/3121357")
aa = driver.find_element_by_css_selector("#novelintro > a")
aa.click()
with open("f:\\temp\\ccp_output0802.html", "w") as ff:
    ff.write(driver.page_source.encode("GBK", "ignore"))

driver.quit()
