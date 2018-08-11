# Zain Tahlilkar, July 2018

from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify


app = Flask(__name__)

# Load Main Page
@app.route("/")
def load_index():
	return render_template('index.html')

# Return Chart Data
@app.route("/chart")
def chart():
	# test: reading month that was sent with request
	month = request.args.get('month')

	# Reading csv file and cleaning up data
	file = open("toronto_historical.csv")
	file_contents = file.readlines()
	toronto_info = file_contents[21:1980]	# lines which have useful data on them
	for i in range(len(toronto_info)):
		toronto_info[i] = toronto_info[i].split(",")
		for j in range(len(toronto_info[i])):
			toronto_info[i][j] = toronto_info[i][j].strip('"')
			print(toronto_info[i])

	# Creating Datasets for chart
	x_labels = []
	high_temps = []
	low_temps = []
	mean_temps= []

	for i in range(len(toronto_info)):
		if int(toronto_info[i][2]) == 6:	# January -- > In the future use a bool array as a mask to filter out which months to show (for yearly trends)
			x_labels.append(toronto_info[i][0])
			high_temps.append(toronto_info[i][3])
			low_temps.append(toronto_info[i][5])
			mean_temps.append(toronto_info[i][7])

	print(month)

	# creating json object
	return jsonify (
		name = "Annual June Temperatures in Toronto",
		mean_temp = mean_temps,
		high_temp = high_temps,
		low_temp = low_temps,
		labels = x_labels
	)




@app.route("/test")
def test():
	file = open("1-1938.csv")
	file_contents = file.readlines()
	tobermory_info = file_contents[161]	#toronto
	tobermory_info = tobermory_info.split(",")
	for i in range(len(tobermory_info)):
		tobermory_info[i] = tobermory_info[i].strip('"')
		print(tobermory_info[i])

	# creating json object
	return jsonify (
		name = tobermory_info[0],
		mean_temp = [1, 2, 3, 2, 1],#float(tobermory_info[4]),
		high_temp = [3, 1, 6, 2, 9],#float(tobermory_info[6]),
		low_temp = [1, 2, 1, 3, 1]#float(tobermory_info[8])
	)


if __name__ == "__main__":
	try:
		app.run(host='0.0.0.0', port=80)
	except:
		print "Server Crashed :("