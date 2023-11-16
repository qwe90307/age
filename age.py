driving = input('請問你有開過車嗎？: ')
if driving != '有' and driving != '沒有':
	print('只能輸入"有"or"沒有"')
	raise SystemExit

age = input('請問你的年齡？: ')
age = int(age)
if driving == '有':
	if age >= 18:
		print('恭喜通過測驗')
	else:
		print('有問題喔')
elif driving == '沒有':
	if age >= 18:
		print('快去考駕照吧!')
	else:
		print('乖小孩')