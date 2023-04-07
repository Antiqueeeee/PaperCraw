import json
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with open("data/english_paper.json",encoding="utf-8") as f:
    english_paper = json.load(f)

download_folder = r"C:\Users\Antique\Downloads"

driver = webdriver.Chrome()
# 中文文献
for paper in english_paper:
    # if int(paper["序号"]) <= 333 or int(paper["序号"]) >= 799:
    #     continue

    driver.get("http://spis.hnlat.com/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="easy-input"]')))
    paper_title = driver.find_element(by=By.XPATH, value='//*[@id="easy-input"]')
    paper_title.send_keys(paper["论文名称"])
    search_btn = driver.find_element(by=By.XPATH, value='//*[@id="search-simple-form"]/button[1]')
    search_btn.click()
    #
    #不行啊好多论文找不到啊
    #
    downloaded = set()
    for root, dirs, files in os.walk(download_folder):
        for file in files:
            downloaded.add(file)
    existed = set()
    #获取下载路径中的文件列表
    #
    #           此处断点
    #           手动选择、下载文献
    #下载完毕，修改文件名
    for root, dirs, files in os.walk(download_folder):
        for file in files:
            existed.add(file)
    new_file = (existed - downloaded).pop()
    paper_name = f'{paper["序号"]}.{paper["第一作者"]}-{new_file}'
    os.rename(
        os.path.join(download_folder, new_file),
        os.path.join(download_folder, paper_name)
    )
