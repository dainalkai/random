import random
r = random.randint(1, 100)
count = 0
while True :
	count += 1
	g = input('請猜一個數字:')
	g = int(g)
	if g == r:
		print('終於猜對了')
		print('總共猜', count ,'次')
		break
	elif g<r :
		print('你猜錯了，答案比', g ,'大')
	else :
		print('你猜錯了，答案比', g ,'小')	
	print('這是猜第', count ,'次')		

	