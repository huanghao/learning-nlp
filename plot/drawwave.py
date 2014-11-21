import wave
import sys
import pylab as pl
import numpy as np


fn = sys.argv[1]
f = wave.open(fn, 'rb')
params = f.getparams()


COL=6
WIDTH=14
SAMPWIDTH2DTYPE = {1: np.int8, 2:np.short}
COLORS = ('b', 'g')

def bar(col=COL, width=WIDTH):
    print '+-%s-+' % '-+-'.join(['-'*width]*col)

def raw(values, col=COL, width=WIDTH):
    print '| %s |' % (' | '.join(['%%-%ds'%width]*col) % values)

bar()
raw(('nchannels', 'sampwidth', 'framerate', 'nframes', 'comptype','compname'))
bar()
raw(params)
bar()

nchannels, sampwidth, framerate, nframes, comptype, compname = params
str_data = f.readframes(nframes)
f.close()


wave_data = np.fromstring(str_data, dtype=SAMPWIDTH2DTYPE[sampwidth])
wave_data.shape = -1, nchannels
wave_data = wave_data.T
time = np.arange(0, nframes) * (1.0 / framerate)

for ichannel in range(nchannels):
    pl.subplot(nchannels, 1, ichannel+1)
    pl.plot(time, wave_data[ichannel], color=COLORS[ichannel])
    pl.ylabel('channel%d'%(ichannel+1))
pl.xlabel('time (seconds)')
pl.show()
