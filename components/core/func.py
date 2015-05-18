import os
from pySmartDL import SmartDL

 # or '~/Desktop/' on linux
def downloadMe(url):
	dest = "./"
	obj = SmartDL(url, dest)
	obj.start()
	return obj.get_dest()
#count_words_at_url("http://mirror.ufs.ac.za/7zip/9.20/7za920.zip")
