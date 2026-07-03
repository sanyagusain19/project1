from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def fetch_hackernews():

    driver = webdriver.Chrome()
    driver.get("https://news.ycombinator.com/")
    time.sleep(3)

    news = []

    rows = driver.find_elements(By.CSS_SELECTOR, "tr.athing")

    for row in rows:

        title = row.find_element(By.CSS_SELECTOR, "span.titleline > a").text

        subtext = row.find_element(By.XPATH, "./following-sibling::tr[1]")

        try:
            score = subtext.find_element(By.CSS_SELECTOR, "span.score").text
        except:
            score = "N/A"

        try:
            comments = subtext.find_element(By.XPATH, ".//a[contains(text(),'comment') or text()='discuss']").text
        except:
            comments = "N/A"

        try:
            post_time = subtext.find_element(By.CSS_SELECTOR, "span.age").text
        except:
            post_time = "N/A"

        news.append({
            "title": title,
            "score": score,
            "comments": comments,
            "time": post_time
        })

    driver.quit()
    return news
