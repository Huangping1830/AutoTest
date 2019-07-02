import numpy
import pandas
import matplotlib.pyplot as plt

ser = pandas.Series(numpy.sin(numpy.linspace(0,7,1000)),index=list(numpy.linspace(0,7,1000)))

asd,as_2 = plt.subplots(figsize=(6,6))

ser.plot(ax=as_2,grid=True,style='.',colormap='Blues_r')

plt.show()