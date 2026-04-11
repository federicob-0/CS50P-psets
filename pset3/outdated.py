def main():
	months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
	month, day, year = get_date("Date: ", months)
	format_date(month, day, year, months)

def get_date(prompt, months):
	while True:
		date = input(prompt).title()
		try:
			month, day, year = date.split("/")
			month, day, year = int(month), int(day), int(year)
		except ValueError:
			pass
		else:
			if year > 0 and 1 <= month <= 12 and 1 <= day <= 31:
				return month, day, year
		try:
			month, day_comma, year = date.split(" ")
			day, year = int(day_comma.replace(",", "")), int(year)
		except ValueError:
			pass
		else:
			if day_comma.endswith(",") and year > 0 and month in months and 1 <= day <= 31:
				return month, day, year

def format_date(month, day, year, months):
	if month not in months:
		print(f"{year:04}-{month:02}-{day:02}")
	else:
		print(f"{year:04}-{months.index(month)+1:02}-{day:02}")

main()
