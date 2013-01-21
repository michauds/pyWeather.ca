import sys, time, bin.fetchTemp as fetchTemp

def main():
	try: 
		sys.argv[1]
		sys.argv[2]
	except: 
		sys.exit("Internal Error")
	
	old_temp = -274
	while True:
		new_temp = fetchTemp.getTemp(sys.argv[1])
		if new_temp != old_temp:
			old_temp = new_temp
			print old_temp
		time.sleep(float(sys.argv[2]))
			
if __name__ == "__main__":
	sys.exit(main())