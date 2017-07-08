#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

from PIL import Image, ImageDraw
from PIL import ImageFont
import datetime, calendar

#cd ext4/YD/code/calendar\ generator/
#./generator.py


def printMonth(year,month,xst,yst,monWidth,draw):
	monHeight 	= monWidth*0.85

	ceilw 	= round(monWidth/7) 									# ширина ячейки, под 7 дней недели
	ceilh 	= round(monHeight/7)										# высота ячеки, 6 недель максимум + название месяца

	#отладочные линии
	draw.line((xst, yst, xst+monWidth, yst), fill="#000000", width=1)
	draw.line((xst, yst, xst, yst+monHeight), fill="#000000", width=1)
	draw.line((xst, yst+monHeight, xst+monWidth, yst+monHeight), fill="#000000", width=1)
	draw.line((xst+monWidth, yst, xst+monWidth, yst+monHeight), fill="#000000", width=1)


	# Написать название месяца
	mnames 	= [u'Январь',u'Февраль',u'Март',u'Апрель',u'Май',u'Июнь',u'Июль',u'Август',u'Сентябрь',u'Октябрь',u'Ноябрь',u'Декабрь']
	font 		= ImageFont.truetype("Gputeks-Regular.ttf", int(monWidth*0.075))
	fsize = font.getsize(mnames[month-1])
	draw.text((xst+(monWidth-fsize[0])/2, yst),mnames[month-1],(0,0,0),font=font) 

	# чуть подвинем циферки
	xst += monWidth*0.03

	(wday,dcount)	= calendar.monthrange(year, month)

	i 		= 1
	strnum 	= 1
	while i<=dcount:
		while wday<7 and i<=dcount:
			draw.text((xst+wday*ceilw, yst+ceilh*strnum),str(i),(0,0,0),font=font)
			i +=1
			wday += 1;
			pass

		wday 	 = 0
		strnum	+= 1

	
	









image 		= Image.new("RGB", (320,320), (255,255,255))
draw 		= ImageDraw.Draw(image)

printMonth(2017,1,30,30,200,draw)
# год, месяц, х , у,  ширина, рисовальщик

image.save("./test.png", "PNG")
del draw

quit()
#-------------------------------------------------





 

num_week = ny_2011.isoweekday()
print(num_week) 




# http://itnote.ru/2010/11/16/python-date-tim/
# кароч сейчас нужна функция, которая рисует месяц по номеру и году





draw.text((10, 10),"Fuck",(0,0,0),font=font)





