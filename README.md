# SMT203_PROJECT
This is a project for the module SMT203 - Smart City Systems Management

Problem statement of our project The current attendance-taking process is unstandardized and inefficient in the age of smart technology. This simple activity has resulted in time wastage amongst professors and teaching assistants.

Our solution

PRESENSE Logo

Before you clone the repo, you should install the correct environment to run the repository. This repository uses the facial_recognition library here: https://github.com/ageitgey/face_recognition/

To set up face_recognition, remember to install cmake.

pip install Pillow pip install face_recognition sudo apt-get update sudo apt-get install -y build-essential sudo apt-get -y install cmake If there is an error, building cmake remeber to download vs_buildtools before running the above command

Follow the instructions here to setup the correct environment for the repository: https://ourcodeworld.com/articles/read/841/how-to-install-and-use-the-python-face-recognition-and-detection-library-in-ubuntu-16-04

After which, pip install cv2, numpy, matplotlib and download an xserver to view the output of the API and follow the instructions here to ensure that it works: http://www.straightrunning.com/XmingNotes/IDH_PROGRAM.htm

Remember to do this if XSERVER doesn't start export DISPLAY=:0.0

Exploring videocapture function with opencv2 https://stackoverflow.com/questions/46387794/how-to-access-webcam-through-opencv-in-bash Currently WSL doesn't seem tom support opening webcam function...
