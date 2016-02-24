"""
This scripts plots the relation between pseudo
count value and classification accuracy.
To execute this file we need to execute
NaiveBayesianClassifier.py first.
If you gauge the pseudo count for several times
with some different files, you could specify the
name of the file that you want to draw, otherwise
the program draw the data in betaAccuracyRelationFile
which contains data of the latest gauge.
The figure is saved in pseudoCountAccuracyRelation.png

"""
import argparse
from matplotlib import pyplot as plt
from numpy import loadtxt
import matplotlib.ticker as m_tick

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", type=str,
                    default="betaAccuracyRelationFile",
                    help="This script will plot the data"
                         "int the file specified by filename."
                         "If filename is not specified, data in "
                         "betaAccuracyRelationFile, namely the"
                         "result of last run of NaiveBayesianClassifier.py"
                         "in gauge mode will be plotted.")
file_name = parser.parse_args().filename
data = loadtxt(file_name)
picture = plt.subplot()
picture.plot(data[:, 0], data[:, 1] * 100)
picture.set_xscale('log')
y_ticks = m_tick.FormatStrFormatter('%.2f%%')
picture.yaxis.set_major_formatter(y_ticks)
plt.xlabel("pseudo count")
plt.ylabel("accuracy")
plt.savefig("pseudoCountAccuracyRelation")

