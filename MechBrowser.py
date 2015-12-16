from mechanize import Browser
from BeautifulSoup import BeautifulSoup


class MechBrowser:
	def __init__(self, url):
		self.browser = Browser()
		self.url = url

	def goTo(self):
		site = self.browser.open(self.url)
		return site

	def source(self):

		html = self.goTo()
		source = BeautifulSoup(html)
		print source


url = 'http://www.digg.com'
br = MechBrowser(url)
br.goTo()

br.source()
