# Album Shen
# Michael Deans Lab
# Johns Hopkins Medicine - Department of Otolaryngology
# 2013 October
#
# Neuron Studio .SWC File Rescaler
#
# Rescales .SWC file with scale (x1, y1, z1) to scale (x2, y2, z2)
# Outputs new .SWC file with same filename + "_RESCALED.swc"

import sys, string, os
from math import pow, sqrt

class SWCRescaler:
	# initialize
	def __init__(self, params):
		global input, scale_in, scale_out, adjust
		global comments, neurites, x_coor, y_coor, z_coor, radius
		global output, output_name
		input = open(params[1], 'rb')
		output = open(params[1].replace('.swc', '_RESCALED.swc'), 'wb')
		output_name = (params[1].replace('.swc', '_output_RESCALED.swc'))
		scale_in = map(float, params[2:5])
		scale_out = map(float, params[5:8])
		adjust = []

		comments = ''
		neurites = []
		x_coor = []
		y_coor = []
		z_coor = []
		radius = []
		
	# counts dendrites and axons for each branch
	# performs position analysis
	# outputs results to output file
	def work(self):

		# read neurites from input
		# n T x y z R P
		comments = ''
		neurites = []
		for line in input.readlines():
			if line.startswith('#'):
				comments = comments + line
				continue
			neurites.append(line.split(" "))
		
		# correct for index at 0
		neurites[0] = [0] * 7
		
		# assigning coordinates arrays
		x_coor = [float(row[2]) for row in neurites]
		y_coor = [float(row[3]) for row in neurites]
		z_coor = [float(row[4]) for row in neurites]
		radius = [float(row[5]) for row in neurites]	

		# find ratios needed to adjust the scales
		adjust = [scale_out[i] / scale_in[i] for i in xrange(3)]
		adjust.append(sqrt(sum(pow(scale_out[i],2) for i in xrange(2)) / sum(pow(scale_in[i],2) for i in xrange(2))))
		# [x, y, z, R]
		
		# multiplying coordinates arrays to adjust the scales
		x_coor = [str(i * adjust[0]) for i in x_coor]
		y_coor = [str(i * adjust[1]) for i in y_coor]
		z_coor = [str(i * adjust[2]) for i in z_coor]
		radius = [str(i * adjust[3]) for i in radius]

		# rewriting neurites matrix with new scale
		for i in xrange(len(neurites)):
			neurites[i] = [neurites[i][0], neurites[i][1], x_coor[i], y_coor[i], z_coor[i], radius[i], neurites[i][6]]
				
		# output rescaled SWC to file
		output.write(comments + '\n'*2)
		for i in xrange(1, len(neurites)):
			output.write(' '.join(neurites[i]))
		
if __name__ == '__main__':
	# read parameters
	# ['SWCRescaler.py', input, x1, y1, z1, x2, y2, z2]
	# input:			.swc file to be read; results will be output to the filename plus the extension '_RESCALED.swc'
	# x1, y1, z1:		original scale
	# x2, y2, z2:		revised scale
	
	# Running with manual input
	# Sample run
	# Rescale = SWCRescaler(['SWCRescaler.py', 'sample.swc', 0.1, 0.1, 0.1, 0.198, 0.198, 0.5])

	# Running through command line
	# ['SWCRescaler.py', input, x1, y1, z1, x2, y2, z2]
	# Rescale = SWCRescaler(sys.argv)
	
	# runs rescaling operations
	# outputs results to output file
	Rescale.work()