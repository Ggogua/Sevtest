import requests

def test_api_get_posts():
    url = "http://localhost:8000/api/posts/" 
    response = requests.get(url) 
    
    
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    
    posts = response.json()  
    assert isinstance(posts, list), "Expected the response to be a list of posts"
    
    assert len(posts) > 0, "Expected at least one post to be returned"
    
    first_post = posts[0]
    assert "title" in first_post, "Expected 'title' field in the post"
    assert "content" in first_post, "Expected 'content' field in the post"
    
    expected_title = "Sample Post" 
    assert first_post["title"] == expected_title, f"Expected title '{expected_title}' but got '{first_post['title']}'"
