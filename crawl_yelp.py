# -*- coding: UTF-8 -*-
import html5lib, requests
from bs4 import BeautifulSoup
from lxml import html

class crawlYelp:

    doctor_count = 0

    def __init__(self):
        crawlYelp.doctor_count += 1

    def get_address(self):
        doctor_url = "https://www.yelp.com/biz/urgent-medical-care-union-square-new-york"

        return doctor_url

    def get_data(self):

        doctor_url = self.get_address()
        wb_data = requests.get(doctor_url)
        soup = BeautifulSoup(wb_data.text,'html5lib')

        # soup = BeautifulSoup(open("C:/Users/Robin/Desktop/yelp.html"),"html5lib")

        doctor_name = soup.select("div.biz-page-header-left.claim-status > div > h1")[0].get_text().split(',')[0].strip()
        doctor_speciality = soup.select("div.biz-main-info.embossed-text-white > div.price-category > span > a")[0].get_text().split(',')[0].strip()
        overall_rating = soup.select("div.biz-rating > div")[0]['title'].split(' ')[0]
        review_number = soup.select("div.biz-rating > span")[0].get_text().strip().split(' ')[0]
        doctor_address_data = soup.select("div > strong > address")[0].get_text()
        doctor_address = ' '.join(doctor_address_data.split())
        doctor_city = doctor_address.split(',')[0].split(' ')[-1]
        doctor_state = doctor_address.split(',')[1].split(' ')[1]
        doctor_zipcode = doctor_address.split(',')[1].split(' ')[2]

        print doctor_name, doctor_speciality, overall_rating, review_number, doctor_address, doctor_city, doctor_state, doctor_zipcode

        page_number = int(review_number) // 20 + 1
        print "Review page:" + str(page_number)
        for i in range(0, page_number):
            page_url = "?start=" + str(20 * i)
            doctor_page_url = doctor_url + page_url
            print doctor_page_url


            for review_data in soup.select(".review--with-sidebar"):
                try:
                    # print review_data
                    reviewer_id = review_data.select('#dropdown_user-name')[0]['href'].split('=')[1]
                    reviewer_name = review_data.select('#dropdown_user-name')[0].get_text().strip()
                    reviewer_address = review_data.select('.user-location')[0].get_text().strip()
                    reviewer_city = review_data.select('.user-location')[0].get_text().strip().split(',')[0]
                    reviewer_state = review_data.select('.user-location')[0].get_text().strip().split(',')[1].strip()

                    rating_score = review_data.select('.i-stars')[0]['title'].split(' ')[0]
                    rating_date = review_data.select('.rating-qualifier')[0].get_text().strip().split(' ')[0].strip()
                    rating_content = review_data.select('p')[0].get_text().strip()
                    rating_useful = review_data.select('.count')[0].get_text().strip()
                    rating_funny = review_data.select('.count')[1].get_text().strip()
                    rating_cool = review_data.select('.count')[2].get_text().strip()

                    print "------------Review------------"
                    print reviewer_id, reviewer_name, reviewer_address, reviewer_city, reviewer_state, rating_score, rating_date, rating_content, rating_useful, rating_cool, rating_funny

                except Exception as err:
                    pass





if __name__ == '__main__':
    crawler = crawlYelp()
    crawler.get_data()