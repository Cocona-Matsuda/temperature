from selenium import webdriver
import time

driver = webdriver.Chrome("c:/temperature/chromedriver.exe")
driver.get("https://forms.office.com/Pages/ResponsePage.aspx?id=XYP-cpVeEkWK4KezivJfyCeFAslPic5ClvPV53svxD1UMERBS0pEU0xGNlUzMlpCQkNYODZSREhVWS4u")
time.sleep(5)

#体温

# 選択肢を出す
element = driver.find_element_by_xpath('//*[@id="Select_0"]/div/i')
element.click()

# 体温を選択
element = driver.find_element_by_xpath('//*[@id="Select_0]/ul/li[1]')
element.click()


#体調

# 咳が出る（いいえ）
element = driver.find_element_by_xpath(
    '//*[@id="form-container"]/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/input')
element.click()
time.sleep(3)

# 喉が痛い（いいえ）
element = driver.find_element_by_xpath(
    '//*[@id="form-container"]/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[4]/input')
element.click()
time.sleep(3)

#体がだるい（いいえ）
element = driver.find_element_by_xpath(
    '//*[@id="form-container"]/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[5]/input')
element.click()
time.sleep(3)

# 頭痛がある（いいえ）
element = driver.find_element_by_xpath(
    '//*[@id="form-container"]/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[6]/input')
element.click()
time.sleep(3)

#送信
element = driver.find_element_by_xpath(
    '// *[@id="form-container"]/div/div/div/div/div/div[2]/div[3]/div/div/div')
element.click()
time.sleep(3)

driver.close()
