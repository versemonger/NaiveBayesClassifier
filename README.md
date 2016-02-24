Executing NaiveBayesianClassifier.py directly will output classification result in file classification_result.txt and the accuracy in the console, the pesudo count will be 1 / |V|, where V is the set of vocabulary.

Option -g starts gauge mode. Options -s, -e, and -n can be used to change the setting of gauge. The detailed instructions are listed below.

	-g, --gaugeMode       	If flag g is used, the program runs in gauge mode and
	                        findsrelation between pseudo counter and accuracy.-m
	                        and -t will not take effect when -g is used.The gauge
	                        result is output in betaAccuracyRelation-s-e-n, where
	                        s, e, n represents start, end, numberrespectively. The
	                        result is also output intobetaAccuracyRelationFile.
	-s START, --start START
		                    Set the starting point for para gauge.Default value is
		                    -5, which corresponds to1e-5
	-e END, --end END       Set the ending point for para gauge.Default value is
	                    	0, which corresponds to 1
	-n NUMBER, --number NUMBER
		                    Set the number of sample points for para gauge.The
		                    sample points distributes in correspondence
		                    tologarithm space. Default value is 50

The following are instructions for other options.

	-b BETA, --beta BETA  Set the parameter for additive smoothing,default value
	                      is 1 / vocabulary_size
	-m, --confusionMatrix
	                      If flag m is used, the program outputs confusion
	                      matrix in format of latex.The output file is
	                      named confusionMatrix.This flag also outputs
	                      classification accuracyof each category in file
	                      categorical_accuracy in format of latex
	-t, --best_words      If flag t is used, the program outputs a list of words
	                      that it mostly relies on in file TopWords. It also
	                      outputs a file named TopWordsCountsInDifferentCategories 
	                      which contains the numerb of key words each category contains


After executing the script NaiveBayesianClassifier.py in gauge mode for at least once, we could execute script plot_relation.py which plots the relation between pseudo counts and accuracy. 
plot_relation.py has one optional argument -f. Its description is as below.

	-f FILENAME, --filename FILENAME
                          This script will plot the dataint the file specified
                          by filename.If filename is not specified, data in
                          betaAccuracyRelationFile, namely theresult of last run
                          of NaiveBayesianClassifier.pyin gauge mode will be
                          plotted.

After executing the script NaiveBayesianClassifier.py with flag -t for at least once, we could execute the script find_bias.py.
This finds the number of top 100 keywords contained by each category and outputs it in the file categorical_key_words.


