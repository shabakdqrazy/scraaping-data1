from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import requests
import pandas as pd
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs#Field_brown_dwarfs"

# Webdriver
browser = webdriver.Chrome()
browser.get(START_URL)
def scrape_more_data(hyperlink):
    print(hyperlink)
    
    ## ADD CODE HERE ##
    try : 
        page = requests.get(hyperlink)
        soup = BeautifulSoup(browser.page_source, "html.parser")
        temp = []
        for tr in soup.find_all("tr",attrs={"class","fact_row"}):
            tdtags = tr.find_all("td",)

            for td in tdtags:
                try:
                    temp.append(td.find_all("div",attrs = {"class","value"})[0].contents[0])
                except:
                    temp.append("")

    except:
        time.sleep(1)
        scrape_more_data(hyperlink)
kkk = pd.DataFrame()

# Convert to CSV
kkk.to_csv('kk.csv',index=True, index_label="id")
