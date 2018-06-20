# Contributors: Prof. Daisuke Kihara, Ziyun Ding, Xi He, Zixuan Liu
# Lab HomePage: http://www.kiharalab.org/
# License: GNU LGPLv3
# https://www.gnu.org/licenses/gpl-3.0.en.html

import numpy as np
import sys

def id_name(inputfile, outputfile):
    proID,clust=np.loadtxt(inputfile,dtype = 'str',skiprows=1,unpack='true')

#build the dictionary, using cluster number as key, protein ID as value 
    id_num=dict()
    for i in range(len(proID)): 
        if int(clust[i]) in id_num:
            id_num[int(clust[i])]+= '\t' +(eval(proID[i]))
        else:
            id_num[int(clust[i])]=eval(proID[i])

    f=open(outputfile, 'w')

#pairwise protein ID within the same cluster
    for key in id_num:
        a=id_num[key].split('\t')
        if len(a)==1:
            a=str(a).replace("[","").replace("'","").replace("]","")
        
            f.write(str(a)+'\t'+str(key)+"\n")
        else:
            for i in range(0, len(a)):
                for j in range(i+1, len(a)):
                    f.write(str(a[i])+ '\t' + str(a[j]) + '\t' + str(key) + "\n")
    f.close

if __name__ == '__main__':
    inputfile=sys.argv[1]
    outputfile=sys.argv[2]
    id_name(inputfile,outputfile)