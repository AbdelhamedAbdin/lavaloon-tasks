def formatDuration(durate):
	year = (365 * 24 * 60 * 60)
	day = (24 * 60 * 60)
	hour = (60 * 60)
	minute = 60
	second = 59
	year_count = 0
	day_count = 0
	hour_count = 0
	min_count = 0
	date = ''
	date_year = ''
	date_day = ''
	date_hour = ''
	date_min = ''
	date_second = ''

	if durate == 0:
		return "now"
	if durate < 0:
		return "must accept a non-negative integer"	
	# year duration
	while durate >= year:
		date_year = ''
		durate = durate - year
		year_count += 1
		if year_count == 1:
			date_year += str(year_count) + " year , "
		elif year_count > 1:
			date_year += str(year_count) + " years , "
		else:
			date_year += ''	
	# day duration
	while durate >= day:
		date_day = ''
		durate = durate - day
		day_count += 1
		if day_count == 1:
			date_day += str(day_count) + " day , "
		elif day_count > 1:
			date_day += str(day_count) + " days , "
		else:
			date_day += ''		
	# hour duration
	while durate >= hour:
		date_hour = ''
		durate = durate - hour
		hour_count += 1
		if hour_count == 1:
			date_hour += str(hour_count) + " hour , "
		elif hour_count > 1:
			date_hour += str(hour_count) + " hours , "
		else:
			date_hour += ''		
	# minute duration
	while durate >= minute:
		date_min = ''
		durate = durate - minute
		min_count += 1
		if min_count == 1:
			date_min += str(min_count) + " minute , "
		elif min_count > 1:
			date_min += str(min_count) + " minutes , "
		else:
			date_min += ''	
	# second duration
	if durate <= second:
		date_second = ''
		if durate == 1:
			date_second += str(durate) + " second"
		else:
			if durate == 0:
				date_second = ''
			else:
				date_second += str(durate) + " seconds"	
	# set , or and 	
	date += date_year + date_day + date_hour + date_min + date_second
	date_split = date.split()
	count_char = date_split.count(",")
	new_date = ''

	if count_char > 1 or count_char == 1:
		for dt in date_split:
			date_split[-3] = "and"

	new_date = " ".join(date_split)

	return new_date		
		
print(formatDuration(1231234345))
print(formatDuration(62))
print(formatDuration(59))
print(formatDuration(0))
print(formatDuration(-59))