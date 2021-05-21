aba =  raw_input('dfghjkl')
b =0
ab = aba.split(':')
if len(ab)==6:
    for i in [0,1,2,3,3,4,5]:
        a = ab[i]
        if len(a) == 2:
            b =i

        else:
            break

    if b == 5:
        print '{}:{}:{}'.format(ab[0],ab[1],ab[2],)

        print 'OK'


