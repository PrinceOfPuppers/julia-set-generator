#julia-set-generator

dependencies:
    -matplotlib
    -numpy

description:
    generates a julia set according to a seedpoint set in config.py

    multiprocessing is used to decrease the image rendering time, this is incredibly helpful due to 
    the large number of iterations needed to obtain a good resolution with certain julia sets 
