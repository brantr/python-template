#import sys
#import os
import numpy as np
#import matplotlib.pyplot as plt
#from astropy.io import fits
#from astropy.wcs import WCS
import argparse
#from tqdm import tqdm
import time

#######################################
# Create command line argument parser
#######################################

def create_parser():

	# Handle user input with argparse
    parser = argparse.ArgumentParser(
        description="Flags and options from user.")

    parser.add_argument('-i', '--input',
        dest='input',
        default='input.fits',
        metavar='input',
        type=str,
        help='Input file to process.')

    parser.add_argument('-v', '--verbose',
        dest='verbose',
        action='store_true',
        help='Print helpful information to the screen? (default: False)',
        default=False)

    return parser

#######################################
# main() function
#######################################
def main():

    #begin timer
    time_global_start = time.time()

    #create the command line argument parser
    parser = create_parser()

    #store the command line arguments
    args   = parser.parse_args()

    #end timer
    time_global_end = time.time()
    if(args.verbose):
    	print(f"Time to execute program: {time_global_end-time_global_start}s.")

#######################################
# Run the program
#######################################
if __name__=="__main__":
	main()