# Contributors: Prof. Daisuke Kihara, Ziyun Ding, Xi He, Zixuan Liu
# Lab HomePage: http://www.kiharalab.org/
# License: GNU LGPLv3
# https://www.gnu.org/licenses/gpl-3.0.en.html

from svmutil import *
import glob
import sys

def predict(inputFile, outputlabel, outputValue):
    y, x = svm_read_problem('../../Ara_ms_data/Aryal_2017_svminput')
    m = svm_load_model('whole_ara_model')
    # p, q = svm_read_problem('../../scoring_functions-master/t6972_svm_input')
    p_label, p_acc, p_val = svm_predict(y, x, m)
    output1 = open('../../Ara_ms_data/Aryal_2017_svm_label', 'w')
    output1.write(','.join(str(e) for e in list(p_label)))
    output2 = open('../../Ara_ms_data/Aryal_2017_svm_val', 'w')
    output2.write(','.join(str(e) for e in list(p_val)))
    output1.close()
    output2.close()

'''
from svmutil import *
y, x = svm_read_problem('../../scoring_functions-master/svm_clust_input')
m = svm_train(y, x, '-c 2 -g 0.0078125 -w1 99.868558 -w0 0.131442 -v 6')
Cross Validation Accuracy = 37.3773%
'''


if __name__ == '__main__':
    inputFile = sys.argv[1]
    label = sys.argv[3]
    value = sys.argv[4]
    predict(inputFile, model, label, value)