#!/usr/bin/env python3

import os
from PIL import Image, ImageDraw, ImageFont
from PyQRNative import *
from verhoeff import *

codesDir = 'codes'
if not os.path.isdir(codesDir):
    os.makedirs(codesDir)

codeFont = ImageFont.truetype("Ubuntu-B.ttf", 80)

bkImg = Image.open("kutyasuli-tagkartya.png")

# retrieving QR codes from range with verhoeff check digit appended.
for i in range(3000,3200):
    code = str(i)+calc_check_digit(i)
    print("Generating QR code: "+code)
    qr = QRCode(2, QRErrorCorrectLevel.H)
    qr.addData(code)
    qr.make()
    qrImg = qr.makeImage()
#    qrImg.save(codesDir+'/'+code+'.png')

    img = bkImg.copy()
    img.paste(qrImg, (87,253))
    draw = ImageDraw.Draw(img)
    draw.text((496,370), code, fill='#02508d', font=codeFont)
    img.save(codesDir+'/kutyasuli-tagkartya-'+code+'.png')
