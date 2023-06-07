from time import time
fpss=[]

for i in range(100):
    start = time()
    for i in range(5000000):
        pass
    fps = 1/(time()-start)
    fpss.append(fps)
av=0
for f in fpss:
    av+=f
av/=len(fpss)
print(f"Average:{av}")