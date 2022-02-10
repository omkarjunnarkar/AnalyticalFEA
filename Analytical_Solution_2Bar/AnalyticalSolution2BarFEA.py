import numpy as np
import os

os.chdir(r"E:\Documents\TU Freiberg CMS\3.Sem-Study Material\PPP\Working_Directory\Analytical_Solution_2Bar")

a1=17
a2=10
l1=32
l2=57
fmax=6000
limit=220
E=120000

outF=open("AnalyticalSolution.txt","w")
outF.write("Force      Sigma1       Sigma2      Eps1        Eps2        U       RF1     RF2")
outF.write("\n")

f=np.linspace(0,fmax,10000)

for force in f:
    
    p2=-force/(((l2*a1)/(l1*a2)) + 1)
    p1=p2+force
    sigma1=p1/a1
    sigma2=p2/a2
    eps1=sigma1/E
    eps2=sigma2/E
    u=eps1*l1
    
    if abs(sigma1)<limit:
        print(force,p1,p2,sigma1,sigma2,u)
        outF.write(str(force))
        outF.write(" ")
        outF.write(str(sigma1))
        outF.write(" ")
        outF.write(str(sigma2))
        outF.write(" ")
        outF.write(str(eps1))
        outF.write(" ")
        outF.write(str(eps2))
        outF.write(" ")
        outF.write(str(u))
        outF.write(" ")
        outF.write(str(p1))
        outF.write(" ")
        outF.write(str(p2))
        outF.write("\n")


outF.close()
