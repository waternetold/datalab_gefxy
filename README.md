# datalab_gefxy
Extract x,y from GEF CPT files

This project is a one hour project for a collegue but maybe useful for others so we decided to share it. The script is simply checking for .gef files in a given path (recursively so underlying paths will be searched as well). It will create a file called geffiles.csv which contains the following columns;

* filepath; the complete path to the file
* filename; the name of the file without the path
* name; the name of the GEF based on the #TESTID that might be given (if not you'll get undefined as the name)
* x; the given x coordinate or -1 if not valid or not found
* y; the given x coordinate or -1 if not valid or not found

That's all there is to it!

## Usage

Use in the commandline with Python by calling

<pre>
python extractxy.py <your path to the gef files>
</pre>

for example;

<pre>
python extractxy.py /home/rob/data/gef
</pre>

Tested on linux.. not on windows because well.. you know.. once you like linux.. :-)

## Maintainer
Rob van Putten | rob.van.putten@waternet.nl or breinbaasnl@gmail.com | 2018 
