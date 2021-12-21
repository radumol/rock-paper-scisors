Rock Paper Scisors game

1) Build the image from the Dockerfile:

docker build -t rps_game .

2) Run the app

docker run -it rps_game

3) Run the unit tests

docker run -it rps_game pytest -v test_rps.py