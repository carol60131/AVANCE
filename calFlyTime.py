# -*- coding: utf-8 -*-
# 依據出發、抵達、日出、日落、結束時間，計算總飛行時間

from datetime import datetime as dt
import datetime


def calFlyTime(liberationDT, arrivalDT, sunriseTime, sunsetTime, endDT, isFix):

	# 不計算夜間時間
	if isFix == 1:

		# 出發日期與抵達日期相同或出發日期與結束日期相同
		if liberationDT.date() == arrivalDT.date() or liberationDT.date() == endDT.date():
			
			if liberationDT.date() == arrivalDT.date():
				# 抵達時間-出發時間
				result = arrivalDT - liberationDT

			else:
				# 結束時間-出發時間
				result = endDT - liberationDT

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
				
				# 出發日期與抵達日期相同或出發日期與結束日期相同
				if liberationDT.date() == arrivalDT.date() or liberationDT.date() == endDT.date():
					break

				else:
					# 日落時間-日出時間
					result += sunsetTime - sunriseTime

			# 最後一日
			if liberationDT.date() == arrivalDT.date() and arrivalDT < endDT:
				# 抵達時間-日出時間 
				result += arrivalDT - sunriseTime

			else:
				# 結束時間-日出時間
				result += endDT - sunriseTime

			resMin = result.total_seconds() / 60 
			return resMin

	# 計算夜間時間
	elif isFix == 2:

		if arrivalDT < endDT:
			# 抵達時間-出發時間
			result = arrivalDT - liberationDT

		else:
			# 結束時間-出發時間
			result = endDT - liberationDT

		resMin = result.total_seconds() / 60 
		return resMin


def main():
	# 出發、抵達時間
	liberationDT = dt.strptime('2024-02-14 08:00:00', '%Y-%m-%d %H:%M:%S')
	arrivalDT = dt.strptime('2024-02-17 17:00:00', '%Y-%m-%d %H:%M:%S')

	# 日出、日落時間
	sunriseTime = dt.strptime('06:00:00', '%H:%M:%S')
	sunsetTime = dt.strptime('18:00:00', '%H:%M:%S')

	# 比賽結束時間
	endDT = dt.strptime('2024-02-17 15:00:00', '%Y-%m-%d %H:%M:%S')

	# 判斷是否計算夜間時間(1:不計算，2:計算)
	isFix = 1

	time = calFlyTime(liberationDT, arrivalDT, sunriseTime, sunsetTime, endDT, isFix)
	print('共飛行', time, '分鐘')


if __name__ == '__main__':
	main()
