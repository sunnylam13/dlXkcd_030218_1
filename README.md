# Download XKCD Comics

A program that can be used to download XKCD webcomics.

## Actions

* loads the XKCD home page

* saves the comic image on said page

* follows the *Previous Comic* link

* repeats until it his the first comic

## Code Actions

* download pages with the `requests` module

* find the URL of the comic image for a page using Beautiful Soup

* download and save the comic image to the hard drive with `iter_content()`

* find the URL of the Previous Comic link and repeat

## Source URL

http://xkcd.com/

## References/Resources

ABSP:  418

