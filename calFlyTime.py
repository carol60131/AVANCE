# -*- coding: utf-8 -*-
# 依據出發、抵達、日出、日落時間，計算總飛行時間

from datetime import datetime as dt
import datetime


def calFlyTime(liberationDT, arrivalDT, sunriseTime, sunsetTime, isFix):

	# 不計算夜間時間
	if isFix == 1:

		# 出發日期與抵達日期相同(抵達時間-出發時間)
		if arrivalDT.date() == liberationDT.date():
			result = arrivalDT - liberationDT
			resMin = result.seconds / 60 

			return resMin		

		else:
			# 將日出、日落時間與出發時間格式化為同日期
			sunriseTime = dt.strptime(str(liberationDT.date()) + ' ' + str(sunriseTime.time()), '%Y-%m-%d %H:%M:%S')
			sunsetTime = dt.strptime(str(liberationDT.date()) + ' ' + str(sunsetTime.time()), '%Y-%m-%d %H:%M:%S')

			# 日落時間-出發時間(第一天)
			result = sunsetTime - liberationDT

			while True:
				# 出發、日出、日落時間加一日
				liberationDT = liberationDT + datetime.timedelta(days=1)
				sunriseTime = sunriseTime + datetime.timedelta(days=1)
				sunsetTime = sunsetTime + datetime.timedelta(days=1)
				
				if arrivalDT.date() == liberationDT.date():
					break

				else:
					# 日落時間-日出時間
					result += sunsetTime - sunriseTime

			# 抵達時間-日出時間(最後一日)
			result += arrivalDT - sunriseTime
			resMin = result.total_seconds() / 60 

			return resMin

	# 計算夜間時間
	elif isFix == 2:

		# 抵達時間-出發時間
		result = arrivalDT - liberationDT
		resMin = result.total_seconds() / 60 

		return resMin


def main():
	# 出發、抵達時間
	liberationDT = dt.strptime('2024-02-14 08:00:00', '%Y-%m-%d %H:%M:%S')
	arrivalDT = dt.strptime('2024-02-17 17:00:00', '%Y-%m-%d %H:%M:%S')

	# 日出、日落時間
	sunriseTime = dt.strptime('06:00:00', '%H:%M:%S')
	sunsetTime = dt.strptime('18:00:00', '%H:%M:%S')

	# 判斷是否計算夜間時間
	isFix = 2

	time = calFlyTime(liberationDT, arrivalDT, sunriseTime, sunsetTime, isFix)
	print('共飛行', time, '分鐘')


if __name__ == '__main__':
	main()
