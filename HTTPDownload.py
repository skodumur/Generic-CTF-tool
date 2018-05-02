#!/usr/bin/python

import urllib

'''
This module takes in an web link of the resource and downloads(with help of urllib) the file from web
it also takes in second parameter which is the new name to the downloaded file
'''

print("starting download")

urllib.urlretrieve("http://trendingmp3.com/music/user_folder/Rae%20Sremmurd%20-%20No%20Flex%20Zone.mp3", "thing.mp3")

print("completed")