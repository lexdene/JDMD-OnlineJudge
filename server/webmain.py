import httplib
from lxml import etree
import subprocess
import urllib
import os
import sys
import getopt

servername = '127.0.0.1'
port = 8080
loginPath = '/user/LoginResult'
submitListPath = '/judgeface/UnjudgeSubmitList'
problemInfoPath = '/judgeface/ProblemInfo'
downloadDataPath = '/judgeface/DownloadData'
sendJudgeResultPath = '/judgeface/JudgeResult'
tempDir = '/tmp/JDMD-OnlineJudge'
codeDirTpl = '%s/code/%d'
dataDirTpl = '%s/data/%d'

reload(sys)
sys.setdefaultencoding('utf8')

def login(loginname,password):
	conn = httplib.HTTPConnection(servername,port)
	
	params = urllib.urlencode(dict(loginname=loginname,password=password))
	headers = dict(Accept='text/html')
	conn.request("POST",loginPath, params, headers)
	
	response = conn.getresponse()
	responseHeaders = response.getheaders()
	cookie=''
	for key,value in responseHeaders:
		if key == 'set-cookie':
			cookie = value
		elif key == 'login-result':
			if value != 'success':
				raise Exception('login failed')
	return cookie

def submitList(cookie):
	conn = httplib.HTTPConnection(servername,port)
	
	headers = dict(Accept='text/html',Cookie=cookie)
	conn.request("GET",submitListPath, headers=headers)
	
	response = conn.getresponse()
	
	parser = etree.XMLParser(remove_blank_text=True,strip_cdata=False)
	doc = etree.parse(response, parser=parser)
	
	result = doc.xpath('result')[0].text
	
	sl = []
	if result == 'success':
		for submit in doc.getiterator('submit'):
			id = int(submit.get('id'))
			pid = submit.get('pid')
			language = submit.find('language').text
			code = submit.find('code').text
			sl.append(dict(
				id=id,
				pid=pid,
				language=language,
				code=code
			))
	else:
		raise Exception('request submit list failed : `%s`'%result)
	
	return sl

def saveCode(s):
	codeDir = codeDirTpl%(tempDir,s['id'])
	if not os.path.exists(codeDir):
		os.makedirs(codeDir)
	
	codeFilePath = '%s/main.cpp'%codeDir
	f = open(codeFilePath,'w')
	f.write(s['code'])
	f.close()
	
	s['codeDir'] = codeDir
	s['codeFilePath'] = codeFilePath
	return True

def compileCode(s):
	binFilePath = '%s/bin'%s['codeDir']
	p = subprocess.Popen(
		["g++",'-o',binFilePath,'-pipe','-O2','-Wall','-W','-DONLINE_JUDGE',s['codeFilePath'] ],
		stdout = subprocess.PIPE,
		stderr = subprocess.PIPE,
	)
	p.wait()
	compileErrorMessage = p.stderr.read(1024*8)
	s['bin'] = binFilePath
	return ( p.returncode == 0,compileErrorMessage)
	
def problemInfo(cookie,pid):
	conn = httplib.HTTPConnection(servername,port)
	
	params = urllib.urlencode(dict(pid=pid))
	headers = dict(Accept='text/html',Cookie=cookie)
	conn.request("POST",problemInfoPath, params , headers)
	
	response = conn.getresponse()
	
	parser = etree.XMLParser(remove_blank_text=True,strip_cdata=False)
	doc = etree.parse(response, parser=parser)
	
	result = doc.xpath('result')[0].text
	
	if result != 'success':
		raise Exception('request problem info failed : %s'%result)
	problem = doc.find('problem')
	return dict(
		pid = int(problem.get('pid')),
		dataCount = int(problem.get('dataCount')),
		time_limit = int(problem.get('time_limit')),
		memory_limit = int(problem.get('memory_limit')),
		authorid = int(problem.get('authorid'))
	)

def downloadData(cookie,problem,dataid,datatype):
	conn = httplib.HTTPConnection(servername,port)
	
	params = urllib.urlencode(dict(
		pid=problem['pid'],
		dataid=dataid,
		datatype=datatype
	))
	headers = dict(Accept='text/html',Cookie=cookie)
	conn.request("POST",downloadDataPath, params , headers)
	
	response = conn.getresponse()
	
	dataDir = dataDirTpl%(tempDir,problem['pid'])
	if not os.path.exists(dataDir):
		os.makedirs(dataDir)
	
	dataFilePath = '%s/%s_%d.dat'%(dataDir,datatype,dataid)
	f = open(dataFilePath,'w')
	f.write(response.read())
	f.close()
	
	return dataFilePath

def runTest(submit,problem,data):
	binFilePath = submit['bin']
	inputFilePath = data['input']
	outputFilePath = '%s/%d.out'%(submit['codeDir'],data['num'])
	errputFilePath = '%s/%d.err'%(submit['codeDir'],data['num'])
	
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
	return True
	
def sendJudgeResult(cookie,result):
	conn = httplib.HTTPConnection(servername,port)
	
	params = urllib.urlencode(result)
	headers = dict(Accept='text/html',Cookie=cookie)
	conn.request("POST",sendJudgeResultPath, params , headers)
	
	response = conn.getresponse()
	
	parser = etree.XMLParser(remove_blank_text=True,strip_cdata=False)
	doc = etree.parse(response, parser=parser)
	
	result = doc.xpath('result')[0].text
	
	if result != 'success':
		raise Exception('request problem info failed : %s'%result)
	else:
		judgeResult = doc.find('judgeResult')
		return dict(
			id=int( judgeResult.get('id') )
		)

def usage():
	print 'usage'
	
def main(argv):
	loginname = ''
	password = ''
	try:
		opts, args = getopt.getopt(argv, "l:p:", ["loginname=", "password=",'server=','port='])
	except getopt.GetoptError:
		usage()
		sys.exit(2)
	for optKey,optValue in opts:
		if optKey in ('-l','--loginname'):
			loginname = optValue
		elif optKey in ('-p','--password'):
			password = optValue
		elif optKey == '--server':
			servername = optValue
		elif optKey == '--port':
			port = optValue
			
	try:
		cookie = login(loginname,password)
		print 'JDMD~ : login success'
		
		sl = submitList(cookie)
		print 'JDMD~ : request submit list success'
		
		for s in sl:
			print 'JDMD~ : begin judge submit %d'%s['id']
			judgeResult = dict(result='accept',sid=s['id'])
			saveCode(s)
			compileResult,compileMessage = compileCode(s)
			judgeResult['compile message'] = compileMessage
			if not compileResult:
				judgeResult['result'] = 'compile error'
			else:
				pi = problemInfo(cookie,s['pid'])
				for i in range(1,pi['dataCount'] +1 ):
					data = dict(
						num=i,
						input=downloadData(cookie,pi,i,'in'),
						output=downloadData(cookie,pi,i,'out')
					)
					runTest(s,pi,data)
				
			print '==== judgeResult ===='
			print judgeResult
			sjr = sendJudgeResult( cookie , judgeResult )
			print '==== send judge result ===='
			print sjr
	except Exception as e:
		print 'Exception:'
		print e

if __name__ == "__main__":
	main(sys.argv[1:])
