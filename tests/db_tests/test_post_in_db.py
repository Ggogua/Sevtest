import sqlite3

def test_post_in_db():
    conn = sqlite3.connect('blog_cms.db')  
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM posts WHERE title = 'Test Blog Post'")
    post = cursor.fetchone()

    assert post is not None 
    assert post[1] == "Test Blog Post"

    conn.close()
