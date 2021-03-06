from selenium import webdriver
import random
import time

class Test():
    def test_case(self):
        driver = webdriver.Chrome()
        driver.get('https://Youtube.com')
        driver.implicitly_wait(10)
        assert driver.title == 'YouTube'
        driver.find_element_by_css_selector('#search').send_keys(random.randint(10, 9999))
        driver.find_element_by_id('search-icon-legacy').click()
        driver.maximize_window()
        time.sleep(6)
        driver.find_elements_by_xpath('//a[@id="video-title"]')[3].click()
        driver.find_element_by_xpath(
            "//yt-img-shadow[@class='style-scope ytd-video-owner-renderer no-transition']/img[@id='img' and @class='style-scope yt-img-shadow' and 1]").click()
        time.sleep(9)
        driver.find_element_by_xpath(
            '//div[@id="subscribe-button"][@class="style-scope ytd-c4-tabbed-header-renderer"]').click()
        alert = driver.find_elements_by_xpath("//yt-formatted-string[text()='Войти']")[2].text
        assert alert == "ВОЙТИ"
        driver.quit()   