"""
This module is used to handle the blog endpoint
"""
from flask import Blueprint, jsonify
from website.models.blog_post import BlogPost

blog = Blueprint(
    name='blog',
    url_prefix='/blog',
    import_name=__name__,
)


@blog.route('/')
def get_posts():
    """Return all the posts available """
    news = list()
    for element in BlogPost.query.all():
        news.append(element.serialize())
    return jsonify({'data': news})


@blog.route('/<post_id>')
def get_post(post_id):
    """Return the specified blog post"""
    element = BlogPost.query.filter(BlogPost.id == post_id).one_or_none()
    return jsonify({'data': element.serialize()})
