# Weather Tracker

## About
Web App that displays historical weather data and trends in Ontario. Made using Python (Flask), and Ajax/Jquery. Charts are made using Chart.js.

Climate data sourced from http://climate.weather.gc.ca

## How to Run
**Note:** You will need Docker to conveniently build and deploy the app.

1. Clone the repository: `git clone https://github.com/zainosaurus/Weather_Tracker`
2. Build the docker image: `docker build -t weather .`
3. Run the docker image: `docker run -it -p 3000:3000 --name weather weather:latest`
4. Access the app in your web browser at `localhost:3000`
