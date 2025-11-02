from flask import url_for

def test_navbar_links_present(client, app):
    """Ensure the navbar has Home, Repos, Blog, Login."""
    # Create an app context so url_for() works
    
    with app.test_request_context():
        url = url_for('home')  # or change this if your route endpoint differs

    response = client.get(url)
    assert response.status_code == 200

    html = response.data.decode()
    assert "Home" in html
    assert "Repos" in html
    assert "Blog" in html
    assert "Logout" in html
