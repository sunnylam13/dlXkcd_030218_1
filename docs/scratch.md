# Scratch

## Friday, March 2, 2018 9:09 PM

The image elements on the site have an `#comic` id (i.e. `<div id="comic">`)

The Prev button has a `rel` HTML attribute with the value `prev`

The first comic's Prev button links to the [http://xkcd.com/#](http://xkcd.com/#) URL, meaning there aren't any more previous pages...

	os.makedirs('xkcd',exist_ok=True) # store comics in ./xkcd

ensures that the folders is real

the `exist_ok=True` stops any exceptions if the folder's already there

