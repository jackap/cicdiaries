from website.models import BlogPost
from datetime import datetime


def test_blog_serialize():
    # Create a BlogPost object with fixed data
    post = BlogPost(
        id=1,
        title="My first post",
        body="This is a test post.",
        created_at=datetime(2024, 5, 10, 14, 30, 0)
    )

    expected = {
        "id": 1,
        "title": "My first post",
        "body": "This is a test post.",
        "created_at": "2024-05-10T14:30:00"
    }

    # Assert that the serialize method returns the expected dict
    assert post.serialize() == expected
