import feedparser
from newspaper import Article


def prase_rss_feeds(rss_feeds):
   feed = feedparser.parse(rss_feeds)
   return feed

def Extract_article_urls(feeds):
    article_urls = []
    for j in feeds.entries:
        article_urls.append(j.link)
    return article_urls


def download_and_parse(url):
    article = Article(url)
    article.download()
    article.parse()
    return article

def extract_article_info(article):
    
    article_info = {
        "title" :article.title,
        "author": article.authors,
        "publish_date" : article.publish_date  
    }
    return article_info


if __name__==  "__main__":

    rss_feeds = "http://feeds.abcnews.com/abcnews/usheadlines"    # other urls http://rss.cnn.com/rss/cnn_topstories.rss , http://www.cbsnews.com/latest/rss/main
        
    feeds = prase_rss_feeds(rss_feeds)
    article_urls = Extract_article_urls(feeds)

    for i, url in enumerate(article_urls):
        try:
            article = download_and_parse(url)
            article_info = extract_article_info(article)
            print(f"Title: {article_info['title']}")
            print(f"Author: {article_info['author']}")
            print(f"Publish Date: {article_info['publish_date'][:20]}")
        except Exception as e:
            print("failed")
