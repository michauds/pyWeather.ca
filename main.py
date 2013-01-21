import sys, time, bin.fetchTemp as fetchTemp

def main():
	try: 
		sys.argv[1]
	except: 
		sys.exit("No city specified")
	
	old_temp = -274
	while True:
		new_temp = fetchTemp.getTemp(sys.argv[1])
		if new_temp != old_temp:
			old_temp = new_temp
			print old_temp
		time.sleep(10)
			
if __name__ == "__main__":
	sys.exit(main())