def hotpo(n,i):
    """

    :rtype : object
    """
    if n>1:
        #print n, " ",
        if n%2==0:
           #Even
           hotpo(n/2,i+1)
        else: #odd
            hotpo(n*3+1,i+1)
    else:
        #print n
        print " Iteration:",i

for i in range(1,4000):
    print "Number: ", i,
    hotpo(i,0)
