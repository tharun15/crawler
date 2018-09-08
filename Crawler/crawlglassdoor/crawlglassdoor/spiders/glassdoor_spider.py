import scrapy


class QuotesSpider(scrapy.Spider):
    name = "glassdoor"
    start_urls = [
        'https://www.glassdoor.co.uk/Reviews/netherlands-reviews-SRCH_IL.0,11_IN178_IP1.htm'
    ]

    def parse(self, response):
        mod_div = response.css(".snug")[0]
        for mod_div in response.css(".snug"):
            yield {
                'Company_name' : mod_div.css(".header.info div:first-child a::text").extract_first(),
                'Company_website' : mod_div.css(".header.info .webInfo .url::text").extract_first(),
                'Rating_nr' : mod_div.css(".ratingsSummary .bigRating::text").extract_first(),
                'Rating_recommend_to_friend' : mod_div.css(".ratingsSummary .minor::text").extract_first(),
                'Number_of_reviews' : mod_div.css(".reviews .num::text").extract_first(),
                'Number_of_salaries' : mod_div.css(".salaries .num::text").extract_first(),
                'Number_of_interviews' : mod_div.css(".interviews .num::text").extract_first(),
            }
        #print(dict(company=Company_name,Company_website=Company_website,Rating_nr=Rating_nr,Rating_recommend_to_friend=Rating_recommend_to_friend,Number_of_reviews=Number_of_reviews,Number_of_salaries=Number_of_salaries,Number_of_interviews=Number_of_interviews))
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        # mod_div = response.url.split("/")[-2]
        # filename = 'glassdoor-%s.html'
        # with open(filename, 'w') as f:
        #     f.write("hello")