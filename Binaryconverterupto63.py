def bnrconv(onum):
  binlist=[]
  bitt=0
  numvar=onum
  if onum<=63 and onum>31:
    binlist=[0,0,0,0,0,1]
    numvar= numvar - 32
    bitt=5
  elif onum<=31 and onum>15:
    binlist=[0,0,0,0,1]
    print binlist
    bitt=4
    numvar-=2**bitt
  elif onum<=15 and onum>7:
    binlist=[0,0,0,1]
    bitt=3
    numvar-=2**bitt
  elif onum<=7 and onum>3:
    binlist=[0,0,1]
    bitt=2
    numvar-=2**bitt
  elif onum<=3:
    binlist=[0,1]
    bitt=1
    numvar-=2**bitt
  else:
    binlist=[1]
  for x in range(bitt+1):
    if numvar>=2**bitt:
      binlist[bitt]=1
      numvar-=2**bitt
      bitt-=1
    else:
      bitt-=1
      
  return binlist[::-1]

print bnrconv(43)