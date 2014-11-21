import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab


def gitlog(path):
    def show(commit, dt):
        cmd = 'git diff -U0 %s^ %s' % (commit, commit)
        diff = os.popen(cmd).read()
        print '|'.join([
            commit,
            dt.strftime('%Y%m%d%H%M%S'),
            str(len(diff)),
            ])

    os.chdir(path)
    for line in os.popen('git log').read().split('\n'):
        if line.startswith('commit'):
            commit = line.split()[1].strip()
        elif line.startswith('Date:'):
            dt = parse(line.split(':', 1)[1].strip())
            show(commit, dt)



def test():
    size = []
    for line in sys.stdin:
        if line.startswith('#'):
            continue
        commit, dt, sz = line.split('|')
        sz = int(sz)/2
        size.append(sz)

    orig = np.array(size)
    mean = orig.mean()
    median = np.median(orig)
    refine = np.array([i for i in orig if i < 10*median])

    ax1 = plt.subplot(311)
    plt.plot(orig)

    plt.subplot(312)
    plt.plot(refine)

    plt.subplot(313)
    plt.hist(refine)

    plt.show()
   

if len(sys.argv) > 1:
    gitlog(sys.argv[1])
else:
    test()
    #plot()
