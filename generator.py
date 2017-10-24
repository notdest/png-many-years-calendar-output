#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

from PIL import Image, ImageDraw
from PIL import ImageFont
import datetime, calendar



def printMonth(year,month,x,y,monthWidth,draw):
	global rus
	monthHeight 	= monthWidth*0.85

	cellWidth 		= round( monthWidth/7 )								# Cell width, for 7 days of the week
	cellHeight 		= round( monthHeight/7 )							# Height of the cell, 6 weeks maximum + name of the month

	# Lines for debugging the geometry of the month
	if 0 :
		draw.line((	x, 				y, 				x+monthWidth, 	y				), fill="#00", width=1)  #  --
		draw.line((	x, 				y, 				x, 				y+monthHeight	), fill="#00", width=1)  #	|
		draw.line((	x, 				y+monthHeight, 	x+monthWidth, 	y+monthHeight	), fill="#00", width=1)  #	_
		draw.line((	x+monthWidth, 	y, 				x+monthWidth, 	y+monthHeight	), fill="#00", width=1)  #	  |


	# Write the name of the month
	if rus :
		names 		= [u'Январь',u'Февраль',u'Март',u'Апрель',u'Май',u'Июнь',u'Июль',u'Август',u'Сентябрь',u'Октябрь',u'Ноябрь',u'Декабрь']
	# Names in English
	else :
		names 	= [u'January',u'February',u'March',u'April',u'May',u'June',u'July',u'August',u'September',u'October',u'November',u'December']
	font 		= ImageFont.truetype("./fonts/Forum-Regular.otf", int(monthWidth*0.075*1.5))
	nameSize 	= font.getsize(names[month-1])
	draw.text(( x+(monthWidth-nameSize[0])/2 , y ), names[month-1], 0, font=font) 

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
			draw.text(( x+ dayOfTheWeek*cellWidth + (maxLength[0]-length[0])/2 , y+ cellHeight*lineNum ),str(i),0,font=fontNumeric )
			i +=1
			dayOfTheWeek += 1;
			pass

		dayOfTheWeek 	 = 0
		lineNum	+= 1

	
def printYear(year,yearOfBirth,x,y,yearWidth,draw):
	global rus
	columnsCount = 6	
	cellWidth 	 = yearWidth/columnsCount
	cellHeight 	 = yearWidth*0.166*0.8

	# Display the name of the year
	yearFont	= ImageFont.truetype("./fonts/Forum-Regular.otf", int(cellWidth*0.85*0.075*3))
	age 		= year - yearOfBirth

	caption 	= str(year)
	if rus : 
		caption += u'г'
	caption 	+= ' 			'+ str(age)

	if rus:
		if age % 10>1 and age % 10<5 and age//10 != 1 :
			caption += u' года'
		elif age % 10==1 and age//10 != 1 :
			caption += u' год'
		else:
			caption += u' лет'
	else :
		if age % 10==1 :
			caption += u' year'
		else:
			caption += u' years'

	captionSize = yearFont.getsize(caption)
	draw.text((x+ (yearWidth-captionSize[0])/2 , y), caption ,0,font=yearFont)
	y 			+= cellWidth*0.85*0.075*4

	# Print the months
	i 				= 1
	lineNumber		= 0
	columnNumber 	= 0
	while i<13:
		printMonth(year,  i,  x+cellWidth*columnNumber,  y+lineNumber*cellHeight,  cellWidth*0.85,  draw)
		columnNumber 	+= 1
		if i%columnsCount == 0:
			lineNumber 	 += 1
			columnNumber = 0
		i 		+=1


def print60Years(yearOfBirth,imageWidth,imageHeight,dpi,draw):
	cellWidth 	= imageWidth*0.2															# width and height of the cell of one year
	cellHeight 	= cellWidth*0.295
	x 			= int(20*dpi/25.4)
	y 			= int(10*dpi/25.4) 															# left and right indents (mm)


	lineNum 	= 0
	columnNum 	= 0
	i 			= 0

	while i<60:
		printYear(yearOfBirth+i, yearOfBirth, x+columnNum*cellWidth, y+lineNum*cellHeight ,cellWidth*0.8, draw)
		i 			+= 1
		columnNum	+= 1
		if columnNum > 4:
			columnNum 	=  0
			lineNum 	+= 1

																							# add copyright
	font 	= ImageFont.truetype("./fonts/BebasNeueLight.ttf", int( cellWidth*0.0085 ))
	draw.text(( x , y + int(cellHeight*0.8) ), 'https://github.com/notdest/png-many-years-calendar', 0, font=font) 




def print80Years(yearOfBirth,imageWidth,imageHeight,dpi,draw):
	cellWidth 	= imageWidth*0.2															# width and height of the cell of one year
	cellHeight 	= cellWidth*0.295
	x 			= int(20*dpi/25.4)
	y 			= int(30*dpi/25.4) 															# left and right indents (mm)


	lineNum 	= 0
	columnNum 	= 0
	i 			= 0

	while i<80:
		printYear(yearOfBirth+i, yearOfBirth, x+columnNum*cellWidth*0.97 , y+lineNum*cellHeight*1.46 ,cellWidth*0.93, draw)
		i 			+= 1
		columnNum	+= 1
		if columnNum > 4:
			columnNum 	=  0
			lineNum 	+= 1

																							# add copyright
	font 	= ImageFont.truetype("./fonts/BebasNeueLight.ttf", int( cellWidth*0.017 ))
	draw.text(( x , y + int(cellHeight*0.95) ), 'https://github.com/notdest/png-many-years-calendar', 0, font=font) 


def print100Years(yearOfBirth,imageWidth,imageHeight,dpi,draw):
	cellWidth 	= imageWidth*0.2															# width and height of the cell of one year
	cellHeight 	= cellWidth*0.295
	x 			= int(20*dpi/25.4)
	y 			= int(30*dpi/25.4) 															# left and right indents (mm)


	lineNum 	= 0
	columnNum 	= 0
	i 			= 0

	while i<100:
		printYear(yearOfBirth+i, yearOfBirth, x+columnNum*cellWidth*0.97 , y+lineNum*cellHeight*1.15 ,cellWidth*0.93, draw)
		i 			+= 1
		columnNum	+= 1
		if columnNum > 4:
			columnNum 	=  0
			lineNum 	+= 1

																							# add copyright
	font 	= ImageFont.truetype("./fonts/BebasNeueLight.ttf", int( cellWidth*0.017 ))
	draw.text(( x , y + int(cellHeight*0.95) ), 'https://github.com/notdest/png-many-years-calendar', 0, font=font) 

#-----------------------------------------------------------------------------------

paperWidth 	= 841 								# vertical sheet orientation
paperHeight = 1189 

dpi 		= 300

yearOfBirth = 1991

rus 		= True

imageWidth 	= int(paperWidth*dpi/25.4)
imageHeight = int(paperHeight*dpi/25.4)



rus 	= True 									# 100 years
i 		= 1917

while i<2017:

	yearOfBirth = i
	image 		= Image.new("L", (imageWidth,imageHeight), 255)
	draw 		= ImageDraw.Draw(image)

	print100Years(yearOfBirth,imageWidth,imageHeight,dpi,draw)

	image.save("./result/rus/100/"+str(yearOfBirth )+"_A0.png", "PNG")
	del draw
	del image
	i += 1

rus 	= False
i 		= 1917

while i<2017:

	yearOfBirth = i
	image 		= Image.new("L", (imageWidth,imageHeight), 255)
	draw 		= ImageDraw.Draw(image)

	print100Years(yearOfBirth,imageWidth,imageHeight,dpi,draw)

	image.save("./result/eng/100/"+str(yearOfBirth )+"_A0.png", "PNG")
	del draw
	del image
	i += 1




quit()


rus 	= True 									# 80 years
i 		= 1937

while i<2017:

	yearOfBirth = i
	image 		= Image.new("L", (imageWidth,imageHeight), 255)
	draw 		= ImageDraw.Draw(image)

	print80Years(yearOfBirth,imageWidth,imageHeight,dpi,draw)

	image.save("./result/rus/80/"+str(yearOfBirth )+"_A0.png", "PNG")
	del draw
	del image
	i += 1

rus 	= False
i 		= 1937

while i<2017:

	yearOfBirth = i
	image 		= Image.new("L", (imageWidth,imageHeight), 255)
	draw 		= ImageDraw.Draw(image)

	print80Years(yearOfBirth,imageWidth,imageHeight,dpi,draw)

	image.save("./result/eng/80/"+str(yearOfBirth )+"_A0.png", "PNG")
	del draw
	del image
	i += 1




paperWidth 	= 1189								# horizontal sheet orientation, 60 years
paperHeight = 841

imageWidth 	= int(paperWidth*dpi/25.4)
imageHeight = int(paperHeight*dpi/25.4)


rus 	= True
i 		= 1957

while i<2017:

	yearOfBirth = i
	image 		= Image.new("L", (imageWidth,imageHeight), 255)
	draw 		= ImageDraw.Draw(image)

	print60Years(yearOfBirth,imageWidth,imageHeight,dpi,draw)

	image.save("./result/rus/60/"+str(yearOfBirth )+"_A0.png", "PNG")
	del draw
	del image
	i += 1

rus 	= False
i 		= 1957

while i<2017:

	yearOfBirth = i
	image 		= Image.new("L", (imageWidth,imageHeight), 255)
	draw 		= ImageDraw.Draw(image)

	print60Years(yearOfBirth,imageWidth,imageHeight,dpi,draw)

	image.save("./result/eng/60/"+str(yearOfBirth )+"_A0.png", "PNG")
	del draw
	del image
	i += 1