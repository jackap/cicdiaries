"""
This module is used to handle the blog endpoint
"""
import markdown
from flask import Blueprint, render_template, abort
from website.models.blog_post import BlogPost

blog = Blueprint(
    name='blog',
    url_prefix='/blog',
    import_name=__name__,
)


@blog.route('/')
def blog_list():
    """Render all the blog posts"""
    posts = BlogPost.query.order_by(BlogPost.created_at.desc()).all()
    return render_template('blog.html', blog_posts=posts)


@blog.route('/<int:post_id>')
def get_post(post_id):
    """Render a single blog post by id"""
    post = BlogPost.query.get_or_404(post_id)
    post_html = markdown.markdown(
        post.body,
        extensions=['fenced_code', 'codehilite', 'tables', 'toc', 'sane_lists']
    )
    return render_template('blog_detail.html', post=post, post_html=post_html)
