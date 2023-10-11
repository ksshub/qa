from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller

path = chromedriver_autoinstaller.install()

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)

# 웹페이지 열기
driver.get("https://illuminarean.com")

# 팝업창 종료
xbtn = driver.find_element(By.CSS_SELECTOR, "body > div.ReactModalPortal > div > div > div > div > button.css-1lby940.e1iwydzj0 > svg")
xbtn.click()

# Work 클릭
work = driver.find_element(By.CSS_SELECTOR, "#__next > div > header > div > div > div > div > nav > ul > li:nth-child(2) > a > span")
work.click()

# GOODVIBE WORKS 클릭
work = driver.find_element(By.CSS_SELECTOR, "#__next > div > main > div > div:nth-child(2) > div > div.css-s49xw9.edcyzk41 > div > a")
work.click()

# 페이지 전환
driver.switch_to.window(driver.window_handles[-1])

# 무료 체험 신청 클릭
muryo = driver.find_element(By.CSS_SELECTOR, "#__next > div > div > header > div > div > ul > li:nth-child(2) > button")
muryo.click()

# 상세 입력
# 회사명
driver.find_element(By.ID, "companyName").send_keys("CompanyName")

# 대표자명
driver.find_element(By.NAME, "ceoName").send_keys("CEOName")

# 사업자 유형 선택
driver.find_element(By.CSS_SELECTOR, "#businessType > div > div.react-select__value-container.react-select__value-container--has-value.css-1hwfws3").click()
option = driver.find_element(By.XPATH, '//*[text()="개인"]')
option.click()

# 사업 규모 선택
driver.find_element(By.CSS_SELECTOR, "#scale > div > div.react-select__value-container.react-select__value-container--has-value.css-1hwfws3").click()
option = driver.find_element(By.XPATH, '//*[text()="51-100 명"]')
option.click()

# 담당자명
driver.find_element(By.NAME, "name").send_keys("sungsookim")

# 이메일
driver.find_element(By.NAME, "email").send_keys("tjdtn0504@naver.com")

# 휴대폰 번호
driver.find_element(By.NAME, "mobile").send_keys("01087042738")

# 담당 업무 1개 선택(직접 선택)
driver.find_element(By.CSS_SELECTOR, "body > div.ReactModalPortal > div > div > div > div > div > div > div > div.css-1c95w5k.e1oaq22c4 > dl.duties > dd > div > div.css-y10ynn.el0tj999 > button > p > div").click()
option = driver.find_element(By.XPATH, '//*[text()="매니저"]')
driver.execute_script("arguments[0].scrollIntoView();", option)
option.click()
option = driver.find_element(By.XPATH,'//*[text()="등록"]')
option.click()
driver.save_screenshot("매니저.png")

# 담당 업무 1개 선택(검색 후 선택)
driver.find_element(By.CSS_SELECTOR, "body > div.ReactModalPortal > div > div > div > div > div > div > div > div.css-1c95w5k.e1oaq22c4 > dl.duties > dd > div > div.css-y10ynn.el0tj999 > button > p > div").click()
driver.find_element(By.CSS_SELECTOR, "body > div.ReactModalPortal > div > div > div > div > div > div > div > div.css-1c95w5k.e1oaq22c4 > dl.duties > dd > div > div.css-y10ynn.el0tj999 > button > p > div > input[type=text]").send_keys("인사")
option = driver.find_element(By.XPATH, '//*[text()="인사"]')
option.click()
option = driver.find_element(By.XPATH,'//*[text()="등록"]')
option.click()
driver.save_screenshot("인사.png")

# 신청 취소 클릭
driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(10) > button").click()

# 신청 취소 팝업창 확인
driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(12) > div > div > div > div > div > div > button:nth-child(2)").click()
