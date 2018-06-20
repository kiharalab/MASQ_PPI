# Contributors: Prof. Daisuke Kihara, Ziyun Ding, Xi He, Zixuan Liu
# Lab HomePage: http://www.kiharalab.org/
# License: GNU LGPLv3
# https://www.gnu.org/licenses/gpl-3.0.en.html

import sys


def get_seq_dic(filepath2):
	seq_dic=dict()
	dict_file=open(filepath2).read().split('//\n')[0:-1]
	for prot in dict_file:
		prot_id=prot.split('\n')[0].split()[1]
		#print prot_id
		prot_seq=''.join(prot.split('SQ   SEQUENCE')[1].split('\n')[1:]).replace(' ','').replace('X','').replace('U','')
		#print prot_seq
		seq_dic[prot_id]=prot_seq
	return seq_dic


def outfiles(filepath1, filepath2, outputfilepath1, outputfilepath2):
	
	ppi_list = open(filepath1).read().split('\n')
	dic = get_seq_dic(filepath2)
	output_id = open(outputfilepath1, 'w')
	output_seq = open(outputfilepath2, 'w')

	for ppi in ppi_list:
		if ppi.split()[0].upper() in dic and ppi.split()[1].upper() in dic:
			if len(dic[ppi.split()[0].upper()]) >= 50 and len(
					dic[ppi.split()[1].upper()]) >= 50:
				output_seq.write(dic[ppi.split()[0].upper()] + ',' + dic[
					ppi.split()[1].upper()] + '\n')
				output_id.write(ppi.split()[0].upper() + '\t' + ppi.split()[1].upper() + '\n')
	output_seq.close()
	output_id.close()


if __name__ == '__main__':
	stepthree_output_filename = sys.argv[1]
	dict_file = sys.argv[2]
	id_file = sys.argv[3]
	seq_file = sys.argv[4]
	outfiles(stepthree_output_filename, dict_file, id_file, seq_file)


