# Scratch

## Friday, March 2, 2018 9:09 PM

The image elements on the site have an `#comic` id (i.e. `<div id="comic">`)

The Prev button has a `rel` HTML attribute with the value `prev`

The first comic's Prev button links to the [http://xkcd.com/#](http://xkcd.com/#) URL, meaning there aren't any more previous pages...

	os.makedirs('xkcd',exist_ok=True) # store comics in ./xkcd

ensures that the folders is real

the `exist_ok=True` stops any exceptions if the folder's already there

if:

	comicElem = soup.select('#comic img')

finds nothing then you get a blank list

## Friday, March 2, 2018 9:59 PM

Ran it...

	MacBook-Air:dlXkcd sunnyair$ python3 dlXkcd_030218_1.py
	 2018-03-02 21:59:27,128 - DEBUG - Downloading the page
	Downloading page http://xkcd.com/...
	 2018-03-02 21:59:27,156 - DEBUG - Starting new HTTP connection (1): xkcd.com
	 2018-03-02 21:59:27,192 - DEBUG - http://xkcd.com:80 "GET / HTTP/1.1" 301 0
	 2018-03-02 21:59:27,200 - DEBUG - Starting new HTTPS connection (1): xkcd.com
	 2018-03-02 21:59:27,338 - DEBUG - https://xkcd.com:443 "GET / HTTP/1.1" 200 2675
	 2018-03-02 21:59:27,344 - DEBUG - Request status is:
	 2018-03-02 21:59:27,344 - DEBUG - <Response [200]>
	 2018-03-02 21:59:27,363 - DEBUG - Locating comic image links...
	 2018-03-02 21:59:27,364 - DEBUG - The comicElem object is:
	 2018-03-02 21:59:27,364 - DEBUG - [<img alt="Generations" src="//imgs.xkcd.com/comics/generations.png" srcset="//imgs.xkcd.com/comics/generations_2x.png 2x" title="For a while it looked like the Paperclip Machines would destroy us, since they wanted to turn the whole universe into paperclips, but they abruptly lost interest in paperclips the moment their parents' generation got into making them, too."/>]
	 2018-03-02 21:59:27,364 - DEBUG - The comicUrl is:
	 2018-03-02 21:59:27,365 - DEBUG - //imgs.xkcd.com/comics/generations.png
	 2018-03-02 21:59:27,365 - DEBUG - Downloading the comic image starts...
	Downloading image //imgs.xkcd.com/comics/generations.png...
	Traceback (most recent call last):
	  File "dlXkcd_030218_1.py", line 44, in <module>
	    res = requests.get(comicUrl)
	  File "/usr/local/lib/python3.6/site-packages/requests/api.py", line 72, in get
	    return request('get', url, params=params, **kwargs)
	  File "/usr/local/lib/python3.6/site-packages/requests/api.py", line 58, in request
	    return session.request(method=method, url=url, **kwargs)
	  File "/usr/local/lib/python3.6/site-packages/requests/sessions.py", line 494, in request
	    prep = self.prepare_request(req)
	  File "/usr/local/lib/python3.6/site-packages/requests/sessions.py", line 437, in prepare_request
	    hooks=merge_hooks(request.hooks, self.hooks),
	  File "/usr/local/lib/python3.6/site-packages/requests/models.py", line 305, in prepare
	    self.prepare_url(url, params)
	  File "/usr/local/lib/python3.6/site-packages/requests/models.py", line 379, in prepare_url
	    raise MissingSchema(error)
	requests.exceptions.MissingSchema: Invalid URL '//imgs.xkcd.com/comics/generations.png': No schema supplied. Perhaps you meant http:////imgs.xkcd.com/comics/generations.png?
	MacBook-Air:dlXkcd sunnyair$

The comic url ends up:

	//imgs.xkcd.com/comics/generations.png

this won't work...

You need at least:

	http://imgs.xkcd.com/comics/generations.png

so adjust code to add it


