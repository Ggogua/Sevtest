from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  
    driver.get("http://localhost:8000/login")  
    yield driver
    driver.quit()

def test_blog_deletion(driver):
    driver.find_element(By.ID, "username").send_keys("testuser123")
    driver.find_element(By.ID, "password").send_keys("password123")
    driver.find_element(By.ID, "login_button").click()

    driver.find_element(By.ID, "post_list").click()  
    
    delete_button = driver.find_element(By.XPATH, "//button[text()='Delete'][@data-post-id='1']")
    delete_button.click()

    driver.find_element(By.ID, "confirm_delete").click()
  
    assert "Test Blog Post" not in driver.page_source
