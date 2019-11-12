v = input("Enter PM2.5 concentration :")
val = float(v)

if (val>0.0 and val<12.1):
	Ilow = 0
	Ihigh = 50
	Clow = 0
	Chigh = 12

if (val>12.1 and val<35.5):
	Ilow = 51
	Ihigh = 100
	Clow = 12.1
	Chigh = 35.4


if (val>35.5 and val<55.5):
	Ilow = 101
	Ihigh = 150
	Clow = 35.5
	Chigh = 55.4


if (val>55.5 and val<150.5):
	Ilow = 151
	Ihigh = 200
	Clow = 55.5
	Chigh = 150.4


if (val>150.5 and val<250.5):
	Ilow = 201
	Ihigh = 300
	Clow = 150.5
	Chigh = 250.4


if (val>250.5 and val<500.5):
	Ilow = 301
	Ihigh = 500
	Clow = 250.5
	Chigh = 500.4

AQI = ((Ihigh - Ilow)/(Chigh - Clow)) * (val - Clow) + Ilow

print(AQI)
