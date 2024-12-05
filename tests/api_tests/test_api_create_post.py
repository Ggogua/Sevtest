import requests

def test_create_blog_post():
    url = "http://localhost:8000/api/posts/"
    data = {
        "title": "New Post via API",
        "content": "This post was created through an API test."
    }
    response = requests.post(url, json=data)
    
    assert response.status_code == 201  
    assert response.json()["title"] == "New Post via API"

