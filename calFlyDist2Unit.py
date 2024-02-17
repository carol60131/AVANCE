# -*- coding: utf-8 -*-
# 飛行速率單位轉換


def calFlyDist2Unit(flyDist, Unit):

	# 公里
	if Unit == 'Km':
		result = flyDist / 0.001

	# 英尺
	elif Unit == 'ft':
		result = flyDist * 0.3048
	
	# 碼
	elif Unit == 'Yrds':
		result = flyDist * 0.9144
	
	# 英哩
	elif Unit == 'Miles':
		result = flyDist * 0.6214 / 0.001

	# 公尺
	else:
		result = flyDist

	return result


def main():
	flyDist2Unit = calFlyDist2Unit(flyDist, Unit)
	print("{:.3f}".format(flyDist2Unit))


if __name__ == '__main__':
	main()
