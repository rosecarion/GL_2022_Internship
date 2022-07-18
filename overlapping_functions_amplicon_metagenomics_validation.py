# overlapping functions from amplicon and metagenomics validation codes

from concurrent.futures import process
from dis import code_info
from enum import Flag
from this import d
from typing import final
from dp_tools.core.check_model import ValidationProtocol, FlagCode, FlagEntry

import os
from re import T
import sys
import argparse
import textwrap
import pandas as pd
import zipfile
import tarfile
import pathlib as path

def check_expected_directories(directory : path):
    """ checks expected directories exist """

    if not os.path.isdir(directory):
        code = FlagCode.HALT
        message = "The directory '" + str(directory) + "' was expected but not found."
        #report_failure("The directory '" + str(directory) + "' was expected but not found.")
    else: 
        code = FlagCode.GREEN
        message = "The directory " + str(directory)+ " exists."
    return {"code": code, "message": message}

def check_for_file_and_contents(file: path):
    """ used by check_fastq_files and check_final_outputs functions """

    if os.path.exists(file): # path exists
            # now checking for content
            if not os.path.getsize(file) > 0: # file is empty
                code = FlagCode.HALT
                message = "The file " + str(file) + " exists, but the file is empty."
            else:
                code = FlagCode.GREEN # path exists and holds content
                message = "The file " + str(file) + " exists and holds content."
    else:
        code = FlagCode.HALT
        message = "The expected file '" + str(file) + "' does not exist."
    return {"code": code, "message": message} 

def check_raw_multiqc_outputs(sample : path, file_prefixes_in_multiqc : path):
    """ makes sure all samples' read files are in the multiqc outputs """

    if not sample in file_prefixes_in_multiqc:
        code = FlagCode.HALT
        message = "The raw multiqc output is missing the expected '" + sample + "' entry."
    else:
        code = FlagCode.GREEN
        message = "The raw multiqc output contains the expected " + sample + " entry."
    return {"code": code, "message": message} 

def check_filtered_multiqc_outputs(sample : path, file_prefixes_in_multiqc : path):

    if not sample in file_prefixes_in_multiqc:
        code = FlagCode.HALT
        message = "The filtered multiqc output is missing the expected '" + sample + "' entry."
    else:
        code = FlagCode.GREEN
        message = "The filtered multiqc output contains the expected " + sample + " entry."
    return {"code": code, "message": message}


def check_general_fasta_format(file : path):

    line_num = 0
    num_headers = 0
    num_seqs = 0

    with open(file) as in_file:

        for line in in_file:

            # keeping track of current line for reporting any problems
            line_num += 1

            if line.strip().startswith(">"):
                num_headers += 1
            else:
                num_seqs += 1

            if num_headers != num_seqs + 1 and num_headers != num_seqs:
                code = FlagCode.HALT
                message = "Fasta file '" + str(file) + "' does not seem to be formatted properly. Problem detected at line " + str(line_num) + "."
            else:
                code = FlagCode.GREEN
                message = "Fasta file " + str(file) + " is formatted properly."
    return {"code": code, "message": message}