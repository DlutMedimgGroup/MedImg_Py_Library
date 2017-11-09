import numpy as np
a = np.arange(0,12)
a.reshape(3,4)
a.tofile("a.bin")
fin=open("a.bin",'rb')
c = np.fromfile(fin, dtype=np.int64,count=3)
c
d = np.fromfile(fin, dtype=np.int64,count=2)
d
d = np.fromfile(fin, dtype=np.int64, count=2)
d