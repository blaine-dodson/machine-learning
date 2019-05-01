
import pandas

import baseline
import textClassifier
import likeClassifier

#header = ['userid','age','gender','ope','con','ext','agr','neu']

##	The baseline classifier
#	@param profileTable the profile table as a DataFrame
#	@param liwcTable the LIWC table as a DataFrame
#	@param relationTable the relation table as a DataFrame
#	@param imagePath a string with the image directory
#	@param textPath a string with the text directory
#	@returns a profile table as a DataFrame
def base(profileTable,liwcTable,relationTable,imagePath,textPath,modulePath):
	results = pandas.DataFrame(index=profileTable['userid'])
	results['age']    = baseline.MEDIAN_AGE
	results['gender'] = baseline.MEDIAN_GENDER
	results['ope']    = baseline.MEAN_OPEN
	results['con']    = baseline.MEAN_CON
	results['ext']    = baseline.MEAN_EXT
	results['agr']    = baseline.MEAN_AGR
	results['neu']    = baseline.MEAN_NEU
	
	return results


##	The baseline classifier
#
#	Results of classifiers should be indexed by userid so that they can be
#	combined
#
#	@param profileTable the profile table as a DataFrame
#	@param liwcTable the LIWC table as a DataFrame
#	@param relationTable the relation table as a DataFrame
#	@param imagePath a string with the image directory
#	@param textPath a string with the text directory
#	@returns a profile table as a DataFrame
def week4(profileTable,liwcTable,relationTable,imagePath,textPath,modulePath):
	results = pandas.DataFrame(index=profileTable['userid'])
	results['age']    = baseline.MEDIAN_AGE
	results['gender'] = baseline.MEDIAN_GENDER
	results['ope']    = baseline.MEAN_OPEN
	results['con']    = baseline.MEAN_CON
	results['ext']    = baseline.MEAN_EXT
	results['agr']    = baseline.MEAN_AGR
	results['neu']    = baseline.MEAN_NEU
	
	
	textResults = textClassifier.genderTree(profileTable,liwcTable)
	results = results.assign(gender=textResults['gender'])
	
	return results



def jakeTesting(profileTable,liwcTable,relationTable,imagePath,textPath,modulePath):
	#results = profileTable
	#results = profileTable
	#print('profileTable')
	#print(profileTable)
	results = pandas.DataFrame(index=profileTable['userid'])
	
	results['age']    = baseline.MEDIAN_AGE
	results['gender'] = baseline.MEDIAN_GENDER
	results['ope']    = baseline.MEAN_OPEN
	results['con']    = baseline.MEAN_CON
	results['ext']    = baseline.MEAN_EXT
	results['agr']    = baseline.MEAN_AGR
	results['neu']    = baseline.MEAN_NEU
	#print('0')
	#print(results)
	likeResults = likeClassifier.likeLogReg(profileTable,relationTable)
	#print('likeResults')
	#print(likeResults)
	results['gender'] = likeResults['gender']
	#print('5')
	#print(results)
	#print(results.count())
	return results


# change this to use a different classifier
classify = jakeTesting

