#!/usr/bin/python

#------ Python blabla where it finds its stuff at PSI
import sys
sys.path.append('/afs/psi.ch/project/sinq/sl5/lib/python')
sys.path.append('/afs/psi.ch/project/sinq/sl5/lib/python2.4/site-packages')

import nxs
import numpy

nf = nxs.open("simple3D.h5", "w5")

nf.makegroup("entry","NXentry")
nf.opengroup("entry","NXentry")

nf.makegroup("data","NXdata")
nf.opengroup("data","NXdata")

a = numpy.zeros((2,3,4),dtype=numpy.int)
val = 0
for i in range(2):
    for j in range(3):
        for k in range(4):
            a[i,j,k] = val
            val = val + 1

nf.makedata("test",'int32',[2,3,4])
nf.opendata("test")
nf.putdata(a)
nf.putattr("signal",1)
nf.closedata()

nf.closegroup()
nf.closegroup()

nf.close()

exit
