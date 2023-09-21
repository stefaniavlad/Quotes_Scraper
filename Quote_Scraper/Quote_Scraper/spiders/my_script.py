import scrapy

# inherit the class that will scrape the data
class myScraper(scrapy.Spider):
    # name for the scraper
    name = 'mycrawler'
    start_urls = ['https://quotes.toscrape.com/']

# define the function that will retrieve the data for the quotes
    def parse(self, response):
        authors = response.css("small.author::text").extract()
        quotes = response.css("span.text::text").extract()
        tags = response.css("a.tag::text").extract()
        tag_link = response.css("a.tag::attr(href)").extract()
        yield {
            "List_Authors": authors,
            "List_Quotes": quotes,
            "List_Tags": tags,
            "List_Tag_Links": tag_link
        }
