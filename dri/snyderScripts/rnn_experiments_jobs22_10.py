import os
import time
#time.sleep(17000)

selectFolds = [1, 3, 5, 7, 9, 11, 13, 15]
#selectFolds = [1, 15, 3, 13]
#selectFolds = [5, 11, 7, 9]
#selectFolds = [3, 7, 15]
#selectFolds = [1, 5, 9, 11, 13]
trials = xrange(0, 10)

nodeType=os.environ.get('RCAC_SCRATCH')
queue=""
if "snyder" in nodeType:
    queue='ribeirob'
if "hammer" in nodeType:
    queue='csit'
queue = 'csit'

#names, 1 - amazon_DVD_20000, 2 - facebook, 3 - amazon_Music_10000
"""
dataSets=["amazon_Music_10000"]
memory =[5]
summaries = [3]
prTypes = ["neutral"]
netTypes=["LSTMPAR"]
singlePRs=[0]
biasselves = ["posneg"]
degrees=[1, 0]
limits=[0]

"""
#dataSets=["amazon_DVD_7500"]
#dataSets=["amazon_DVD_7500"]
#dataSets=["IMDB_5"]
#dataSets = ["amazon_DVD_20000", "facebook"]
#dataSets=["amazon_Music_64500"]
#dataSets=["amazon_Music_7500"]
#dataSets=["amazon_DVD_20000", "amazon_Music_64500"]
#dataSets=["amazon_Music_7500"]
#dataSets=["amazon_DVD_7500", "amazon_DVD_20000"]
dataSets = ["amazon_Music_64500", "amazon_Music_7500"]
#dataSets=["amazon_DVD_7500", "amazon_DVD_20000", "amazon_Music_64500", "amazon_Music_7500"]
#dataSets = ["patents_computers_50attr"]
memory =[10]
summaries = [3]
prTypes = ["neutral"]
netTypes=["LSTM"]
singlePRs=[0]
biasselves = ["none"]
degrees=[1]
limits=[0]
usePrevWeights=[1]
noDeg0s = [1]
#dataAug=["none"]
dataAug=["none"]
#dataAug=["swapdown", "swap"]
#dataAug=["swapdown"]
#dataAug=["none", "swap", "swapdown"]
#dataAug=["swap", "swapdown"]
#dataAug=["attr", "attrdown"]
#dataAug=["none", "swap", "swapdown", "attr", "attrdown"]
#dataAug = ["attr", "swap", "attrup", "attrdown", "swapup", "swapdown"]
#dataAug = ["swapTriple", "swapQuad"]
#dataAug = ["swapup", "swapdown"]
randInit = [0]
#usePRs = ["for"]
usePRs = ["F"]
gpus = ["cpu"]
#PostFix="PPR"
#PostFix="N2V"
PostFix=""
buildStr='./parallel_commands '
for nettype in netTypes:
    for mem in memory:
        for prtype in prTypes:
            for singlepr in singlePRs:
                for bias in biasselves:
                    for deg in degrees:
                        for limit in limits:
                            for summ in summaries:
                                for weight in usePrevWeights:
                                    for deg0 in noDeg0s:
                                        for aug in dataAug:
                                            for test in dataSets:
                                                for rinit in randInit:
                                                    for usepr in usePRs:
                                                        for gpu in gpus: 
                                                            for trial in trials:
                                                                for fold in selectFolds:
                                                                    submitStr="qsub -q "+queue+" -v nettype='" + str(nettype)+"',mem='" +str(mem)+"',prtype='" + prtype + "',singlepr='"+str(singlepr) + "',test='"+str(test) + "',bias='" + bias + "',deg='" + str(deg) + "',limit='" +str(limit)+ "',summ='"+str(summ)+"',weight='"+str(weight)+ "',nodeg='" +str(deg0) + "',aug='" + str(aug) + "',rinit='" +str(rinit) + "',usepr='" + str(usepr)  + "',gpu='" + str(gpu) +  "',trial='"+str(trial)+"',fold='"+str(fold)+  "' rnn_exp32_10"+PostFix+".sub"
                                                                    print(submitStr)
                                                                    os.system(submitStr)
