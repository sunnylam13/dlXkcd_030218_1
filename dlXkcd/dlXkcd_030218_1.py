# -*- coding: utf-8 -*-

#! python3
# ! /usr/local/Cellar/python3/3.6.1

import requests, os, bs4, logging
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
# logging.disable(logging.CRITICAL)

url = 'http://xkcd.com/' # starting url

os.makedirs('xkcd',exist_ok=True) # store comics in ./xkcd

while not url.endswith('#'):
	# TODO:  download the page
	# TODO:  find the URL of the comic image
	# TODO:  download the image
	# TODO:  save the image to ./xkcd
	# TODO:  get the Prev button's url

print('Done')