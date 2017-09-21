import numpy as np
import sys

def main(srtart, stop, n, filename):
    xsamples = np.linspace(start, stop, n)
    ysamples = np.sin(2*xsamples)
    with open (filename, 'w') as f:
        for (x, y) in zip(xsamples, ysamples):
            f.write('%.5f %.5f\n' % (x, y))

if __name__ == '__main__':
    start = float(sys.argv[1])
    stop  = float(sys.argv[2])
    nsamples = int(sys.argv[3])
    filename = sys.argv[4]
    main(start, stop, nsamples, filename)

