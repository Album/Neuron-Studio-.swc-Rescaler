SWC Rescaler
===================
by Album Shen

Converts a .swc file (used for neurites tracings in NeuronStudio) from one voxel scale to another.

### Parameters ###
* ['SWCRescaler.py', input, x1, y1, z1, x2, y2, z2]
* input:			.swc file to be read; results will be output to the filename plus the extension '_RESCALED.swc'
* x1, y1, z1:		original voxel scale
* x2, y2, z2:		revised voxel scale

### BEFORE USE DO ONE OF THE FOLLOWING ###
* Uncomment line 87 below "# Sample run" to allow for manual entry of input filename and pertinent scales directly into the script. Script can be run using "python SWCRescaler.py" at the command line or simply clicking to execute.

* Uncomment line 90 below "# Running through command line" to run by passing parameters through command line. 
