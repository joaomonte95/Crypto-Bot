import requests
from bs4 import BeautifulSoup
import json

class Scraping(BeautifulSoup):
    def __init__(self):
        self.request = requests.get('https://coinmarketcap.com')
        self.page_content = self.request.content
        self.soup = BeautifulSoup(self.page_content,"html.parser")

    def __return_list_by_tag(self,element_tag,element_class):
        tag_list = self.soup.find_all(element_tag,element_class)
        requested_list = []
        for element in tag_list:
            if element.text[-3::] == "...":
                element_temp = element.text
                element_temp = element_temp.split('...')
                #menor valor = 13.
                requested_list.append(element_temp[0].lower())
            else:
                requested_list.append(element.text.lower())
        return requested_list

    def main(self):
        names_list = self.__return_list_by_tag("a","currency-name-container")
        prices_list = self.__return_list_by_tag("a","price")
        volume_list = self.__return_list_by_tag("a","volume")
        change_list = self.__return_list_by_tag("td","percent-change")
        data = []
        iterations = len(names_list)
        for i in range(iterations):
            data.append({"rank":i+1,"name":names_list[i],"price":prices_list[i],"volume":volume_list[i],"change":change_list[i]})
        return data
