#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

from PIL import Image, ImageDraw
from PIL import ImageFont
import datetime, calendar



def printMonth(year,month,xst,yst,monWidth,draw):
	monHeight 	= monWidth*0.85

	ceilw 	= round(monWidth/7) 									# ширина ячейки, под 7 дней недели
	ceilh 	= round(monHeight/7)										# высота ячеки, 6 недель максимум + название месяца

	#отладочные линии
	if 0 :
		draw.line((	xst, 			yst, 			xst+monWidth, 	yst				), fill="#000000", width=1)  #  --
		draw.line((	xst, 			yst, 			xst, 			yst+monHeight	), fill="#000000", width=1)  #	|
		draw.line((	xst, 			yst+monHeight, 	xst+monWidth, 	yst+monHeight	), fill="#000000", width=1)  #	_
		draw.line((	xst+monWidth, 	yst, 			xst+monWidth, 	yst+monHeight	), fill="#000000", width=1)  #	  |


	# Написать название месяца
	mnames 	= [u'Январь',u'Февраль',u'Март',u'Апрель',u'Май',u'Июнь',u'Июль',u'Август',u'Сентябрь',u'Октябрь',u'Ноябрь',u'Декабрь']
	font 		= ImageFont.truetype("./fonts/Forum-Regular.otf", int(monWidth*0.075*1.5))
	fsize = font.getsize(mnames[month-1])
	draw.text((xst+(monWidth-fsize[0])/2, yst),mnames[month-1],(0,0,0),font=font) 

	# чуть подвинем циферки
	xst += monWidth*0.03

	(wday,dcount)	= calendar.monthrange(year, month)

	fontcifr 	= ImageFont.truetype("./fonts/BebasNeueLight.ttf", int(monWidth*0.075))
	mlen 		= fontcifr.getsize(str(30))		# циферки будут по правому краю, это максимальная длина 
	yst 		+= ceilh*0.4  					# чутка хочу сдвинуть название от чисел

	i 		= 1
	strnum 	= 1
	while i<=dcount:
		while wday<7 and i<=dcount:
			rlen 	= fontcifr.getsize(str(i))
			draw.text((xst+wday*ceilw+(mlen[0]-rlen[0])/2, yst+ceilh*strnum),str(i),(0,0,0),font=fontcifr )
			i +=1
			wday += 1;
			pass

		wday 	 = 0
		strnum	+= 1

	
def printYear(year,byear,xst,yst,yearWidth,draw):
	stlb 		= 6	
	ceilWidt 	= yearWidth/stlb
	ceilHeight 	= yearWidth*0.166*0.8

	# Выводим название года
	yfont		= ImageFont.truetype("./fonts/Forum-Regular.otf", int(ceilWidt*0.85*0.075*3))
	vozr 		= year-byear
	capt 		= str(year)+u'г 			'+ str(vozr)
	if vozr % 10>1 and vozr % 10<5 and vozr//10 != 1 :
		capt += u' года'
	elif vozr % 10==1 and vozr//10 != 1 :
		capt += u' год'
	else:
		capt += u' лет'

	ysize 		= yfont.getsize(capt)
	draw.text((xst+(yearWidth-ysize[0])/2, yst), capt ,(0,0,0),font=yfont)
	yst 		+= ceilWidt*0.85*0.075*4

	# Выводим месяцы
	i 		= 1
	strn 	= 0
	stlbn 	= 0
	while i<13:
		printMonth(year,i,xst+ceilWidt*stlbn,yst+strn*ceilHeight,ceilWidt*0.85,draw)

		stlbn 	+= 1
		if i%stlb == 0:
			strn 	+= 1
			stlbn 	= 0

		i 		+=1

#-----------------------------------------------------------------------------------

paperWidth 	= 1189
paperHeight = 841

dpi 		= 72

bYear 		= 1991

imageWidth 	= int(paperWidth*dpi/25.4)
imageHeight = int(paperHeight*dpi/25.4)

image 		= Image.new("RGB", (imageWidth,imageHeight), (255,255,255))
draw 		= ImageDraw.Draw(image)

ceilWidt 	= imageWidth*0.2
ceilHeight 	= ceilWidt*0.295
xst 		= int(imageWidth*(20/float(paperWidth)))
yst 		= int(imageWidth*(10/float(paperWidth)))


ystr 	= 0
ystlb 	= 0
i 		= 0

while i<60:
	printYear(bYear+i,bYear,xst+ystlb*ceilWidt,yst+ystr*ceilHeight,ceilWidt*0.8,draw)
	i 		+= 1
	ystlb	+= 1
	if ystlb > 4:
		ystlb 	=  0
		ystr 	+= 1


# год, месяц, х , у,  ширина, рисовальщик

image.save("./result/full.png", "PNG")
del draw
