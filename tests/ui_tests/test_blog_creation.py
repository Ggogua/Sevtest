from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import os
CMS_URL = os.getenv("CMS_URL", "http://localhost:8000")

@pytest.fixture
def driver():
    driver = webdriver.Chrome() 
    driver.get(f"{CMS_URL}/login") 
    yield driver
    driver.quit()

def test_blog_creation(driver):
    driver.find_element(By.ID, "username").send_keys("testuser123")
    driver.find_element(By.ID, "password").send_keys("password123")
    driver.find_element(By.ID, "login_button").click()
    driver.find_element(By.ID, "create_post").click()
    driver.find_element(By.ID, "title").send_keys("Test Blog Post")
    driver.find_element(By.ID, "content").send_keys("This is a test blog post content.")
    driver.find_element(By.ID, "submit_post").click()
    assert "Test Blog Post" in driver.page_source
