# Copyright 2018 Rob van Putten
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished
# to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

__author__ = "Rob van Putten"
__copyright__ = "Copyright 2018"
__credits__ = [""]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Rob van Putten"
__email__ = "rob.van.putten@waternet.nl" 
__status__ = "Production"

import glob
import os, sys

def insensitive_glob(pattern):
    """Extract file with glob in a case insensitive way"""
    def either(c):
        return '[%s%s]'%(c.lower(),c.upper()) if c.isalpha() else c
    return glob.glob(''.join(map(either,pattern)))

def get_info(gefdata):
    """Extract GEF information from the given lines"""
    name, x, y = "undefined", -1., -1.
    for line in gefdata:
        if line.find('#TESTID') > -1:
            name = line.split('=')[-1].strip()
        elif line.find('#XYID') > -1:
            args = [a.strip() for a in line.split('=')[-1].split(',') if len(a.strip()) > 0]
            try:
                x = float(args[1])
                y = float(args[2])
            except:
                pass # dan niet!

    return name, x, y

if __name__=="__main__":
    # check of er een argument wordt meegegeven
    if len(sys.argv) != 2:
        print("Fout: ongeldige aanroep, gebruik python extractxy.py <pad naar de gef bestanden>")
        sys.exit(1)

    # check of het pad bestaat
    path = sys.argv[1]
    if not os.path.exists(path):
        print("Fout: De opgegeven directory kon niet gevonden worden.")
        sys.exit(1)

    # maak een uitvoerfile klaar
    f_out = open("geffiles.csv", 'w')
    f_out.write("filepath,filename,name,x,y\n")

    # zoek de bestanden
    globexpression = os.path.join(path, "*.gef")
    files = insensitive_glob(globexpression)

    # als je veel bestanden hebt geef dan een soort van progressie aan
    showprogress = len(files) > 100

    for i in range(len(files)):
        lines = open(files[i], 'r').readlines()
        name, x, y = get_info(lines)
        f_out.write("%s,%s,%s,%.2f,%.2f\n" % (files[i], os.path.basename(files[i]), name, x, y))

        if showprogress and i%100==0:
            print("Bezig met bestand %d uit %d" % (i, len(files)))

    f_out.close()
