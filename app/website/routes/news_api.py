"""
This module is used to handle the news endpoint
"""
from flask import Blueprint, jsonify
from website.models.news import News
from website.connection import db
news = Blueprint(
    name='news_api',
    url_prefix='/api/news',
    import_name=__name__,
)


@news.route('/')
def get_news():
    """Get all the news"""
    news_list = list()
 
    for element in db.session.query(News).all():
        news_list.append(element.serialize())
    return jsonify({'data': news_list})
