#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

from PIL import Image, ImageDraw
from PIL import ImageFont
import datetime, calendar

#cd ext4/YD/code/calendar\ generator/
#./generator.py


def printMonth(year,month,draw):
	monWidth 	= 200
	monHeight 	= 100

	ceilw 	= round(monWidth/7) 									# ширина ячейки, под 7 дней недели
	ceilh 	= round(monWidth/7)										# высота ячеки, 6 недель максимум + название месяца

	# Написать название месяца
	mnames 	= ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь']
	font 		= ImageFont.truetype("Gputeks-Regular.ttf", 15)
	draw.text((10, 10),mnames[month-1],(0,0,0),font=font)

	(wday,dcount)	= calendar.monthrange(2017, 6)

	i 		= 1
	strnum 	= 1
	while i<=dcount:
		while wday<7 and i<=dcount:
			draw.text((10+wday*ceilw, 10+ceilh*strnum),str(i),(0,0,0),font=font)
			#print(wday,monWidth,10+wday*monWidth, 10)
			i +=1
			wday += 1;
			pass

		wday 	 = 0
		strnum	+= 1

	

	#draw.text((10, 10),"Fuck",(0,0,0),font=font)
	









image 		= Image.new("RGB", (320,320), (255,255,255))
draw 		= ImageDraw.Draw(image)

printMonth(2017,6,draw)

image.save("./test.png", "PNG")
del draw

quit()
#-------------------------------------------------





 

num_week = ny_2011.isoweekday()
print(num_week) 




# http://itnote.ru/2010/11/16/python-date-tim/
# кароч сейчас нужна функция, которая рисует месяц по номеру и году





draw.text((10, 10),"Fuck",(0,0,0),font=font)





