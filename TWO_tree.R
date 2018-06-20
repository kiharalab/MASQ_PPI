# Contributors: Prof. Daisuke Kihara, Ziyun Ding, Xi He, Zixuan Liu
# Lab HomePage: http://www.kiharalab.org/
# License: GNU LGPLv3
# https://www.gnu.org/licenses/gpl-3.0.en.html

# The input file format needs to be the tab delimited text file.
# The first column contains the protein ID, the rest of columns are normalized MS data.
# The clustering method could be average, complete, single, ward and so on.
# the number_clust is the number of expected cluster. It should be integer.
# The output indicates the output filename.
clust_protein <- function(file, method, number_clust, output){
  input_data <- read.table(file, sep='\t', header = TRUE)
  d = dist(h) # calculate distance
  tree = hclust(d, method) # build tree
  plot(tree, labels = h$X1)
  cut = cutree(tree, k = number_clust, labels(h$X1))
  write.table(cut, file = output, sep = "\t")
}

