import request 
from urllib.request import urlretrieve, urlopen
from bs4 import BeautifulSoup
import time 
# Getting Movie Codes of Top 5
url = 'http://movie.naver.com/movie/sdb/rank/rmovie.nhn'
page = urlopen(url)
soup = BeautifulSoup(page, "html.parser")
selecting = soup.select('td > div > a')

movie_code = []
for i in selecting[0:5]:
	x = str(i).split('code=')
	y = x[1][:6]
	movie_code.append(y)

while True :
	for i in movie_code :
		img_url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code={}'.format(i)

		img_page = urlopen(img_url)
		img_soup = BeautifulSoup(img_page, "html.parser")
		findImg = img_soup.find('div', attrs={'class':'poster'})

		one_split = str(findImg).split('src="')
		juso = one_split[-1].split('?')[0]


		urlretrieve(juso, "./test{}.jpg".format(movie_code.index(i)+1))

	time.sleep(2)


