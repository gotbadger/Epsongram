# Epsongram
Print images from any website with opengraph image tags. Designed to work with instagram. This was hacked together so sorry to your eyeballs if you read the source.

## Hardware
* Epson TM-T88IIP
* Raspberry pi zero
* Generic USB to Parallel IEEE 1284 Printer Cable aka 36-pin Parrallel Adapter

## Setup
install imagemagick
```
pip3 install -r requirements.txt
python3 main.py
```
go to http://127.0.0.1:8080


NB: This is should not be exposed to the internet...


## Example
Output from TM-T88IIP

![example](https://github.com/gotbadger/Epsongram/blob/master/example.jpg)

## Thanks
[python-escpos](https://github.com/python-escpos/python-escpos) does all the heavy lifting here and is a really nice project for working with printers like this.
