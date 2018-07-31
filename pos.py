import sys
import os
import time
from ftfy import fix_text
from opengraph import OpenGraph
import urllib.request
from escpos import printer

class Pos:
    def __init__(self, url):
        og = OpenGraph(url)
        file_name, headers = urllib.request.urlretrieve(og.image)
        # call image magick to update file in place
        # cmd = 'mogrify -colorspace Gray -ordered-dither h4x4a -resize 512 %s' % file_name
        cmd = 'mogrify -colorspace Gray -resize 512 -unsharp 0x1 %s' % file_name
        os.system(cmd)
        # make an attempt to shorten the title and make it printable
        title = ascii(fix_text(og.title.split('Instagram post by ').pop().split('Instagram: ').pop())).replace('\\u2022','-').replace('\'','')
        p = printer.File("/dev/usb/lp0")
        p.text(title)
        p.text("\n")
        time.sleep(2)
        p.image(file_name)
        time.sleep(2)
        p.text("\n")
        p.text(og.url)
        p.cut()
        print(title)
        print(file_name)
        urllib.request.urlcleanup()
