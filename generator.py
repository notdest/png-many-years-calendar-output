#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

from PIL import Image, ImageDraw
from PIL import ImageFont
import datetime, calendar



def printMonth(year,month,x,y,monthWidth,draw):
	monthHeight 	= monthWidth*0.85

	cellWidth 		= round( monthWidth/7 )								# Cell width, for 7 days of the week
	cellHeight 		= round( monthHeight/7 )							# Height of the cell, 6 weeks maximum + name of the month

	# Lines for debugging the geometry of the month
	if 0 :
		draw.line((	x, 				y, 				x+monthWidth, 	y				), fill="#000000", width=1)  #  --
		draw.line((	x, 				y, 				x, 				y+monthHeight	), fill="#000000", width=1)  #	|
		draw.line((	x, 				y+monthHeight, 	x+monthWidth, 	y+monthHeight	), fill="#000000", width=1)  #	_
		draw.line((	x+monthWidth, 	y, 				x+monthWidth, 	y+monthHeight	), fill="#000000", width=1)  #	  |


	# Write the name of the month
	names 		= [u'Январь',u'Февраль',u'Март',u'Апрель',u'Май',u'Июнь',u'Июль',u'Август',u'Сентябрь',u'Октябрь',u'Ноябрь',u'Декабрь']
	# Names in English
	# names 	= [u'January',u'February',u'March',u'April',u'May',u'June',u'July',u'August',u'September',u'October',u'November',u'December']
	font 		= ImageFont.truetype("./fonts/Forum-Regular.otf", int(monthWidth*0.075*1.5))
	nameSize 	= font.getsize(names[month-1])
	draw.text(( x+(monthWidth-nameSize[0])/2 , y ), names[month-1], (0,0,0), font=font) 

	# Figures should be moved slightly to the right
	x += monthWidth*0.03

	(dayOfTheWeek,daysCount)	= calendar.monthrange(year, month)

	fontNumeric = ImageFont.truetype("./fonts/BebasNeueLight.ttf", int(monthWidth*0.075))
	maxLength 	= fontNumeric.getsize('30')								# Maximum length of the day of the month
	y 			+= cellHeight*0.4  										# Posted numbers a little lower

	i 			= 1
	lineNum 	= 1
	while i<=daysCount:
		while dayOfTheWeek<7 and i<=daysCount:
			length 	= fontNumeric.getsize(str(i))
			draw.text(( x+ dayOfTheWeek*cellWidth + (maxLength[0]-length[0])/2 , y+ cellHeight*lineNum ),str(i),(0,0,0),font=fontNumeric )
			i +=1
			dayOfTheWeek += 1;
			pass

		dayOfTheWeek 	 = 0
		lineNum	+= 1

	
def printYear(year,byear,x,y,yearWidth,draw):
	stlb 		= 6	
	ceilWidt 	= yearWidth/stlb
	ceilHeight 	= yearWidth*0.166*0.8

	# Выводим название года
	yfont		= ImageFont.truetype("./fonts/Forum-Regular.otf", int(ceilWidt*0.85*0.075*3))
	vozr 		= year - byear
	capt 		= str(year)+u'г 			'+ str(vozr)
	if vozr % 10>1 and vozr % 10<5 and vozr//10 != 1 :
		capt += u' года'
	elif vozr % 10==1 and vozr//10 != 1 :
		capt += u' год'
	else:
		capt += u' лет'

	ysize 		= yfont.getsize(capt)
	draw.text((x+(yearWidth-ysize[0])/2, y), capt ,(0,0,0),font=yfont)
	y 		+= ceilWidt*0.85*0.075*4

	# Выводим месяцы
	i 		= 1
	strn 	= 0
	stlbn 	= 0
	while i<13:
		printMonth(year,i,x+ceilWidt*stlbn,y+strn*ceilHeight,ceilWidt*0.85,draw)

		stlbn 	+= 1
		if i%stlb == 0:
			strn 	+= 1
			stlbn 	= 0

		i 		+=1

def print60years(bYear,imageWidth,imageHeight,draw):
	ceilWidt 	= imageWidth*0.2
	ceilHeight 	= ceilWidt*0.295
	x 		= int(imageWidth*(20/float(paperWidth)))
	y 		= int(imageWidth*(10/float(paperWidth)))


	ystr 	= 0
	ystlb 	= 0
	i 		= 0

	while i<60:
		printYear(bYear+i,bYear,x+ystlb*ceilWidt,y+ystr*ceilHeight,ceilWidt*0.8,draw)
		i 		+= 1
		ystlb	+= 1
		if ystlb > 4:
			ystlb 	=  0
			ystr 	+= 1

#-----------------------------------------------------------------------------------

paperWidth 	= 1189
paperHeight = 841

dpi 		= 72

bYear 		= 1991


imageWidth 	= int(paperWidth*dpi/25.4)
imageHeight = int(paperHeight*dpi/25.4)

image 		= Image.new("RGB", (imageWidth,imageHeight), (255,255,255))
draw 		= ImageDraw.Draw(image)



print60years(bYear,imageWidth,imageHeight,draw)

image.save("./result/"+str(bYear )+"_A0.png", "PNG")
del draw
