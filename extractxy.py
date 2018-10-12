import glob
import os, sys

def insensitive_glob(pattern):
    def either(c):
        return '[%s%s]'%(c.lower(),c.upper()) if c.isalpha() else c
    return glob.glob(''.join(map(either,pattern)))

def get_info(gefdata):
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
    if len(sys.argv) != 2:
        print("Fout: ongeldige aanroep, gebruik python extractxy.py <pad naar de gef bestanden>")
        sys.exit(1)

    path = sys.argv[1]
    if not os.path.exists(path):
        print("Fout: De opgegeven directory kon niet gevonden worden.")
        sys.exit(1)

    f_out = open("geffiles.csv", 'w')
    f_out.write("filepath,filename,name,x,y\n")

    globexpression = os.path.join(path, "*.gef")
    files = insensitive_glob(globexpression)

    showprogress = len(files) > 100

    for i in range(len(files)):
        lines = open(files[i], 'r').readlines()
        name, x, y = get_info(lines)
        f_out.write("%s,%s,%s,%.2f,%.2f\n" % (files[i], os.path.basename(files[i]), name, x, y))

        if showprogress and i%100==0:
            print("Bezig met bestand %d uit %d" % (i, len(files)))

    f_out.close()
