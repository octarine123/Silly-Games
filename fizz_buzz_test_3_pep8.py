#!/usr/bin/env python

# modules
import sys
import os
import logging
import timeit
import time

# 4th soluton to implement program with user inputs to vary range of fizz buzz
# include debug log file and runtime

# def global constants
title = "Fizz Buzz Program, Version 3, User Functionality"
b = 0    # end of range
i = 1    # initial iterator
logging.basicConfig(filename='Fizz_buzz_Log.txt',
                    level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
fizz_list = []    # empty fizz matrix
buzz_list = []    # empty buzz matrix
fizz_count = 0    # number of multiples of 3 counted
buzz_count = 0    # number of multiples of 5 counted

logging.disable(logging.CRITICAL)      # turn on/off debug mode
logging.debug('Start of program')

# lists
nolist = [
   "no", "n"
   ]
yeslist = [
   "yes", "yeah", "y"
   ]


# setup
def fizz_buzz():
    global start, stop, runtime
    global fizz_count, buzz_count, i
    global fizz_list, buzz_list
    start = timeit.default_timer()
    while i <= b:
        if (i % 3 == 0):
            print("fizz")
            i += 1
            fizz_count += 1
            logging.debug(str(i)
                          + ' converted to fizz')
            logging.debug('fizz = '
                          + str(fizz_count))
            logging.debug('buzz = '
                          + str(buzz_count))
            fizz_list.append(i)
        elif (i % 5 == 0):
            print("buzz")
            i += 1
            buzz_count += 1
            logging.debug(str(i)
                          + ' converted to buzz')
            logging.debug('fizz = '
                          + str(fizz_count))
            logging.debug('buzz = '
                          + str(buzz_count))
            buzz_list.append(i)
        else:
            print(i)
            i += 1
            stop = timeit.default_timer()
            runtime = float(round(stop - start, 3))


# closed loop for user entry without crashing code
def user_entry():
    global b
    try:    # error handling loop to prevent crashing
        b = int(input("How long do you want the fizz buzz sequence to run?"))
        logging.debug('function range selected ' + str(b))
    except Exception as e:
        logging.debug(str(e))
        print(e)
        # b = 100    # forced sequence range
        user_entry()     # reset point in case of error
        # print('Continuing with b = 100')


def main():
    user_entry()
    fizz_buzz()
    print('runtime is ' + str(runtime) + 's')
    print('Total fizz = ' + str(fizz_count))
    print('Total buzz = ' + str(buzz_count))
    print("list of fizz numbers " + str(fizz_list))
    print("list of buzz numbers " + str(buzz_list))
    logging.debug('End of program')
    logging.debug('Program runtime ' + str(runtime) + 's')
    # reset program to beginning or quit
    reset = input("Do you wannt to start again (y/n)?").lower()
    if reset in yeslist:
        main()
    else:
        raise SystemExit


if __name__ == "__main__":
    try:
        print("Start" + " " + str(title))
        main()
        logging.disable(logging.CRITICAL)
    except KeyboardInterrupt:
        print('Program aborted.')
        logging.disable(logging.CRITICAL)
        raise SystemExit
