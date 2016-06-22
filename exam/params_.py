import requests
import re
from bs4 import BeautifulSoup


class Site():
	def __init__(self, url):
		self.url = url
		self.name = re.findall('(\w+\.\w+)\/', url)[0]

	def parse(self):
		r = requests.get(self.url)
		r.encoding = 'utf-8'
		return BeautifulSoup(r.text, 'html.parser')

	def get_top(self):
		soup = self.parse()
		container = soup.find(self.container_tag, attrs=self.container_attrs)
		top_titles = container.find_all(self.title_tag, attrs=self.title_attrs)
		top_authors = container.find_all(self.authors_tag, attrs=self.authors_attrs)
		return top_titles, top_authors


class LiveLib(Site):
	def __init__(self, url):
		Site.__init__(self, url)
		self.title_tag, self.title_attrs = 'a', {'class': "tag-book-title"}
		self.container_tag, self.container_attrs = 'table', {'class': "linear-list"}
		self.authors_tag, self.authors_attrs = 'a', {'class': 'tag-book-author'}


class ReadRate(Site):
	def __init__(self, url):
		Site.__init__(self, url)
		self.title_tag, self.title_attrs = 'div', {'class': "title"}
		self.container_tag, self.container_attrs = 'div', {'class': "books-list"}
		self.authors_tag, self.authors_attrs = 'li', {'class': 'contributor item'}


class Libs(Site):
	def __init__(self, url):
		Site.__init__(self, url)
		self.title_tag, self.title_attrs = 'h2', {}
		self.container_tag, self.container_attrs = 'div', {'class': "posts doocode_book_result_filter"}
		self.authors_tag, self.authors_attrs = 'div', {'class': 'uk-width-10-10 uk-width-medium-5-10  uk-width-large-5-10'}

	def get_top(self):
		top_titles, top_authors = Site.get_top(self)
		top_libs_authors = []
		for i in top_authors:
			author = i.find('a')
			if author is not None:
				top_libs_authors.append(author)
		top_libs_authors.insert(26, 'error')
		return top_titles, top_libs_authors

"""
class Readly(Site):
	def __init__(self, url):
		Site.__init__(self, url)
		self.title_tag, self.title_attrs = 'h3', {'class': 'blvi__title'}
		self.container_tag, self.container_attrs = 'div', {'class': 'book-list-view'}
"""
