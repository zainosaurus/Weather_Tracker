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
		mean_temp = float(tobermory_info[4]),
		high_temp = float(tobermory_info[6]),
		low_temp = float(tobermory_info[8])
	)


if __name__ == "__main__":
	try:
		app.run(host='0.0.0.0', port=80)
	except:
		print "Server Crashed :("