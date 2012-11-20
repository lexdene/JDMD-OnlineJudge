# -*- coding: utf-8 -*-

import subprocess

class JudgerBase(object):
	def __init__(self):
		pass
		
	def languageList(self):
		return []
		
	def judge(self,submit,problemInfo,dataList):
		judgeResult = dict(result='accept',sid=submit['id'])
		
		# compile
		compileResult = self.compile(submit)
		judgeResult.update( compileResult )
		if judgeResult['result'] != 'accept':
			return judgeResult
		
		for i in dataList:
			dataFile = dataList[i]
			
			# run test
			judgeResult.update( self.runTest(submit,problemInfo,dataFile) )
			
			if judgeResult['result'] != 'accept':
				break
		return judgeResult
		
	def compile(self,submit):
		return dict()
		
	def runTest(self,submit,problemInfo,dataFile):
		binFilePath = submit['bin']
		inputFilePath = dataFile['input']
		outputFilePath = '%s/%d.out'%(submit['codeDir'],dataFile['num'])
		errputFilePath = '%s/%d.err'%(submit['codeDir'],dataFile['num'])
		
		inputFile = open( inputFilePath ,'r')
		outputFile = open( outputFilePath ,'w')
		errputFile = open( errputFilePath ,'w')
		p = subprocess.Popen(
			[ binFilePath ],
			stdin=inputFile,
			stdout=outputFile,
			stderr=errputFile
		)
		inputFile.close()
		outputFile.close()
		errputFile.close()
		return dict()
