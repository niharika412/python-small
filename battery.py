from win10toast import ToastNotifier
toaster = ToastNotifier()

import psutil

def getpercent():
	battery = psutil.sensors_battery()
	plugged = battery.power_plugged
	percent = str(battery.percent)
	return percent

x=getpercent()
while(int(x)>30):
	pass 

toaster.show_toast("Notification","Battery Low!", duration=60)
	
	