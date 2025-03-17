"""
This module is used to handle the news endpoint
"""
from flask import Blueprint, render_template
from website.models.news import News
from website.connection import db
repos = Blueprint(
    name='repos',
    url_prefix='/repos',
    import_name=__name__,
)


@repos.route('/')
def get_repos():
    """Get all the repositories"""
    news_list = list()
 
    for element in db.session.query(News).all():
        news_list.append(element.serialize())
    return  render_template('repos.html',news_list=news_list)
