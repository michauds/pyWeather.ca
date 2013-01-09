import sys, time, fetchTemp



def main():
	if sys.argv is None:
		print "Invalid call"
	else:
		while True:
			temp = fetchTemp.getTemp(sys.argv[1])
			print temp
			time.sleep(10)

if __name__ == "__main__":
	sys.exit(main())