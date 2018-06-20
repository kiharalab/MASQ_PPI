# Contributors: Prof. Daisuke Kihara, Ziyun Ding, Xi He, Zixuan Liu
# Lab HomePage: http://www.kiharalab.org/
# License: GNU LGPLv3
# https://www.gnu.org/licenses/gpl-3.0.en.html

import sys

def peakShiftFilter(inputFile, outputFile):
	with open(inputFile) as whole_file, open(outputFile) as opt:
		n = 0
		whole_file_content = whole_file.read().split('\n')[1:]
		for each in whole_file_content:
			genebanks_protID = each.split('\t')[2].split('|')[3]
			# print genebanks_protID
			# need to change the index of MS profile
			bio1_fractions = map(float, each.split('\t')[3:23])
			bio1_max = max(bio1_fractions)
			bio1_maxpos = bio1_fractions.index(bio1_max)
			norm_bio1_fractions = map(str, [x / bio1_max for x in bio1_fractions])
			# need to change the index of MS profile
			bio2_fractions = map(float, each.split('\t')[25:45])
			bio2_max = max(bio2_fractions)
			bio2_maxpos = bio2_fractions.index(bio2_max)
			norm_bio2_fractions = map(str, [y / bio2_max for y in bio2_fractions])

			# print norm_bio1_fractions

			if abs(bio1_maxpos - bio2_maxpos) <= 2:
				# print each
				n = n + 1
				opt.writelines(genebanks_protID + '\t' + '\t'.join(norm_bio1_fractions) + '\t' + '\t'.join(norm_bio2_fractions))
	whole_file.close()
	opt.close()

if __name__ == '__main__':
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]



