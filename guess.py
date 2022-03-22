# 產生一個隨機整數1~100不要印出來
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "終於答對了!"
# 猜錯的話 要告訴他 比答案大/小

import random
count = 0
start = input('請決定範圍開始值: ')
end = input('請決定範圍結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
while True:
	count += 1 #count = count + 1
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('終於答對了!')
		print('這是你猜的', count, '次')
		break
	elif num > r:
		print('比答案大')
		print('這是你猜的', count, '次')
	elif num < r:
		print('比答案小')
		print('這是你猜的', count, '次')


    



	
