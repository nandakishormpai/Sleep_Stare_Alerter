# Sleep_Stare_Alerter
An openCV driven project to help users stop sleeping and staring into the screen for too long by alerting them.<br>
We used the concept of EAR to do this.

Clone this repo and execute the python file alerter.py along with command line arguement for --shape-predictor.<br> As ::  
alerter.py --shape-predictor shape_predictor_face_landmarks.dat


<h1>Prerequisites</h1><br>
<b>1.</b> opencv<br>
<b>2.</b> numpy<br>
<b>3.</b> argparse<br>
<b>4.</b> imutils<br>
<b>5.</b> dlib<br>
<b>6.</b> pygame<br><br>

<i>It would be better if you do all this in a virtual environment.</i><br>

<h2>The dlib library installation in this is the important part</h2><br>
<B>For windows </b><br><br>
<b><i>Step 1</i></b>: Install Visual Studio 2015 build tools (<1GB) from https://download.microsoft.com/download/5/f/7/5f7acaeb-8363-451f-9425-68a90f98b238/visualcppbuildtools_full.exe<br><br>
<b><i>Step 2</i></b>: Install CMake v3.8.2 from https://cmake.org/download/<br><br>
<b><i>Step 3</i></b>: Install Anaconda 3(not necessary)<br><br>
<b><i>Step 4</i></b>: pip install dlib<br><br>

<b><i> All other libraries can be pip installed</i></b><br>

<b>For Ubuntu and macOS : </b>
<br>
https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf
