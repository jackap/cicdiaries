from website.models import News, BlogPost


def test_news_serialize():
    news = News(description="sample description",
                name='name',
                html_url='www.fake-website.com',
                image_url="self.image_url",
                date="self.date",
                argument="self.argumen")
    news_expected = {'argument': 'self.argumen',
                     'date': 'self.date',
                     'description': 'sample description',
                     'html_url': 'www.fake-website.com',
                     'image_url': 'self.image_url',
                     'name': 'name'}
    assert news.serialize() == news_expected


def test_blog_serialize():
    blogpost = BlogPost(body="sample body",
                        news=News(description="sample description",
                                  name='name',
                                  html_url='www.fake-website.com',
                                  image_url="self.image_url",
                                  date="self.date",
                                  argument="self.argumen"))
    blogpost_expected = {
        'body': "sample body",
        'news': {
            'argument': 'self.argumen',
            'date': 'self.date',
            'description': 'sample description',
            'html_url': 'www.fake-website.com',
            'image_url': 'self.image_url',
            'name': 'name'}}
    assert blogpost.serialize() == blogpost_expected
