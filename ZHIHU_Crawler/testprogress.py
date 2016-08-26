from multiprocessing import Pool
import os, random, time

def long_time_tesk(name):
    print 'run task %s (%s)' % (name, os.getpid())
    start_time = time.time()
    time.sleep(random.random() * 3)
    end_time = time.time()
    print "name is %s, starttime is %s, endtime is %s" % (name, start_time, end_time)

if __name__ == '__main__':
    print 'parent progress pid is ' + str(os.getpid())
    p = Pool()
    for i in range(0, 5):

        p.apply_async(long_time_tesk, args=(i,))
    print 'Waiting for all progress done..'
    p.close()
    p.join()
    print 'All subprogress done!'
