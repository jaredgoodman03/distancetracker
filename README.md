# distancetracker
High school Environmental Club project that finds the average distance each student commutes to school

My High school's Environmental Club was doing a project to caclulate how much gas everybody uses by driving to school every day. This little Python script I made lets you input a file with everybody's address (I got this file through downloading a PDF of the school directory, converting it to a txt, and running grep), and uses the Google Maps API to determine how much people drive. 

## Instructions
1. Download by running `git clone https://github.com/jaredgoodman03/distancetracker.git` in your terminal or pressing "download zip" on this Github page.
2. You'll need python3 and pip3 to install packages. Downloading these is left as an exersise for the reader.
3.  Install [this](https://github.com/googlemaps/google-maps-services-python) Python library by running `pip3 install -U googlemaps`.
4. You'll need a Google Cloud API Key - the package mentioned above has great instructions. Make sure to enable the Directions API. 
5. Copy and paste your API key into params/API_KEY
6. Enter the path of your file to process in params/FILE_PATH. It should have one address on each line.
7. `python3 create_dump.py` to output the distances of each address into a new file called distancedump.txt
8. `python3 calc_average.py` to get basic stats about your data.
9. Make a cool graph (text files can be imported into Excel or Libreoffice pretty easily)
