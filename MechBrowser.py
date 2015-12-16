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

	def forms(self,num=0):
		form = self.browser.select_form(nr = num)





url = 'http://harmonixmusic.com/games/rock-band/request/'
br = MechBrowser(url)
br.goTo()

#br.source()

#br.forms()


'''

url = 'http://harmonixmusic.com/games/rock-band/request/'
br = Browser()
html = br.open(url)
br.select_form(nr = 0)
br.form['title'] = 'hard to see'
br.form['artist'] = 'five finger death punch'
response = br.submit()

content = response.read()
soup = BeautifulSoup(content)
    
p = soup.find('p')
print ''
print p 
print ' '
'''
