from selenium import webdriver
import time
import subprocess
import re
import json

# JSON読み込み
json_open = open('settings.json','r')
json_load = json.load(json_open)
mail = json_load['mail']
pwd = json_load['password']
url = json_load['url']

# Chrom操作
driver = webdriver.Chrome(executable_path='C:./chromedriver.exe')
driver.get(url)
driver.implicitly_wait(10)


# アカウント名
element = driver.find_element_by_xpath(
    '/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/input[1]')
element.click()
element.send_keys(mail)
driver.implicitly_wait(10)

element = driver.find_element_by_xpath('/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div[4]/div/div/div/div/input').click()
driver.implicitly_wait(10)

# パスワード
element = driver.find_element_by_xpath(
    '/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/input')
element.click()
element.send_keys(pwd)
driver.implicitly_wait(10)

element = driver.find_element_by_xpath('/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div/div/input').click()
driver.implicitly_wait(10)

# 多要素認証
cmd = 'cloak.exe view rrr'
process = (subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True).communicate()[0]).decode('utf-8')

element = driver.find_element_by_xpath(
    '/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/div/div[3]/div/input')
element.send_keys(process)
driver.implicitly_wait(10)


# サインインの状態を維持しますか？
driver.find_element_by_xpath('/html/body/div/form/div/div/div[1]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div[1]/input').click()
driver.implicitly_wait(10)



# 選択肢を出す
driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/i').click()
driver.implicitly_wait(10)

# 体温を選択
driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/ul/li[4]').click()
driver.implicitly_wait(10)


#体調

# 咳が出る（いいえ）
driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/input').click()
driver.implicitly_wait(10)

# 喉が痛い（いいえ）
driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[3]/div[3]/input').click()
driver.implicitly_wait(10)

#体がだるい（いいえ）
driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[4]/div[3]/input').click()
driver.implicitly_wait(10)

# 頭痛がある（いいえ）
driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[5]/div[3]/input').click()
driver.implicitly_wait(10)

#送信
driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[1]/div[2]/div[3]/div[1]/button/div').click()
driver.implicitly_wait(10)

