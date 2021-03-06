# -*- coding: utf-8 -*-

#! python3
# ! /usr/local/Cellar/python3/3.6.1

import requests, os, bs4, logging
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
logging.disable(logging.CRITICAL)

url = 'http://xkcd.com/' # starting url

os.makedirs('xkcd',exist_ok=True) # store comics in ./xkcd

while not url.endswith('#'):
	# download the page
	logging.debug('Downloading the page')
	print('Downloading page %s...' % url)
	res = requests.get(url)
	res.raise_for_status()
	logging.debug('Request status is:  ')
	logging.debug(res)

	soup = bs4.BeautifulSoup(res.text,"html.parser")
	# logging.debug('The requests object is:  ')
	# logging.debug(soup)

	# find the URL of the comic image
	logging.debug('Locating comic image links...')
	comicElem = soup.select('#comic img')
	logging.debug('The comicElem object is:  ')
	logging.debug(comicElem)

	if comicElem == []:
		print("Could not find comic image.")
	else:
		comicUrl = "http:" + comicElem[0].get('src') # find the src attribute and get its value
		# the selector should contain a list with only one image element because there's only one image on the page
		logging.debug('The comicUrl is:  ')
		logging.debug(comicUrl)

	# download the image
	logging.debug('Downloading the comic image starts...')
	print("Downloading image %s..." % (comicUrl))
	res = requests.get(comicUrl)
	res.raise_for_status()

	# save the image to ./xkcd
	logging.debug('Saving the image file to ./xkcd')
	imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
	for chunk in res.iter_content(100000):
		imageFile.write(chunk)
	imageFile.close()

	# get the Prev button's url
	logging.debug('Get the Prev button url')
	prevLink = soup.select('a[rel="prev"]')[0] # the first match using [0]
	url = 'http://xkcd.com' + prevLink.get('href')
	logging.debug('Prev button url is:  ')
	logging.debug(url)

print('Done')