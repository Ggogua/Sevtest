from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  
    driver.get("http://localhost:8000/login")  
    yield driver
    driver.quit()

def test_blog_view(driver):
    driver.find_element(By.ID, "username").send_keys("testuser123")
    driver.find_element(By.ID, "password").send_keys("password123")
    driver.find_element(By.ID, "login_button").click()

    driver.find_element(By.ID, "post_list").click()  

    driver.find_element(By.XPATH, "//a[text()='Test Blog Post']").click()  

    assert "Test Blog Post" in driver.page_source
    assert "This is a test blog post content." in driver.page_source 
