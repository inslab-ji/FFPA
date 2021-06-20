import time

def printRound(i):
    print('==================================')
    print('             Round %d             ' % i)
    print('==================================')

def printLog(args,performance):
    timestemp = str(time.strftime('%Y.%m.%d-%H:%M:%S',time.localtime(time.time())))
    record = timestemp + ';'
    record += '%s;' % str(args.dataset)
    record += '%s;' % str(args.mode)
    record += 'precision=%.4f;' % performance[0]
    record += 'recall=%.4f;' % performance[1]
    record += 'dup=%d;' % args.duplicate
    record += 'm=%d;' % args.num_participants
    record += 'epsilon=%.1f;' % args.epsilon

    if args.mode == 'ffpa':
        if args.orig_k > 1:
            record += 'k=%d;' % args.k
        else:
            record += 'k=%.2f;' % args.orig_k
        record += 'xi=%.2f;' % args.xi
        record += 'c=%d;' % args.num_candidate
        record += 'max_support=%d;' % args.max_support
    
    record += '\n'
    return record