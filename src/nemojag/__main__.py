#!/usr/bin/env python3
import sys
from nemojag.app import create_app

'''
The main function. Main code should go here.
'''
def main(args):
    print("Hello World!")
    create_app().run()

if __name__ == "__main__":
    val = main(sys.argv)
    exit()