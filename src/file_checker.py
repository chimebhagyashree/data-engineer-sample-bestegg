# Author : Bhagyashree Nayak
# Date : 08/15/2021
# version : 1
""" This program will create a class for checking files in the provided path"""
# ************************Change#:1********************************
# Change(s) Made: Initial build
# Date of Change: 08/15/2021
# Author: Bhagyashree Nayak
# Change Approved by: Bhagyashree Nayak
# Date Moved to Production: 08/15/2021
# ******************************************************************
import os
import glob


class check_files:
    def get_files(filepath: str):
        all_files = []
        for root, dirs, files in os.walk(filepath):
            files = glob.glob(os.path.join(root, '*.txt'))
            for f in files:
                all_files.append(os.path.abspath(f))
        return all_files
