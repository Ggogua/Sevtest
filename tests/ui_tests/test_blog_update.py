from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  
    driver.get("http://localhost:8000/login")  
    yield driver
    driver.quit()

def test_blog_update(driver):
   
    driver.find_element(By.ID, "username").send_keys("testuser123")
    driver.find_element(By.ID, "password").send_keys("password123")
    driver.find_element(By.ID, "login_button").click()

   
    driver.find_element(By.ID, "post_list").click()

   
    edit_button = driver.find_element(By.XPATH, "//button[text()='Edit'][@data-post-id='1']") 
    edit_button.click()

 
    title_field = driver.find_element(By.ID, "title")
    title_field.clear()
    title_field.send_keys("Updated Blog Post Title")

    content_field = driver.find_element(By.ID, "content")
    content_field.clear()
    content_field.send_keys("Updated content for the blog post.")

    driver.find_element(By.ID, "submit_post").click()

    assert "Updated Blog Post Title" in driver.page_source
    assert "Updated content for the blog post." in driver.page_source
