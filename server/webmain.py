import httplib
from lxml import etree
import subprocess
import urllib
import os

servername = '127.0.0.1'
port = 8080
loginPath = '/user/LoginResult'
submitListPath = '/judgeface/UnjudgeSubmitList'
problemInfoPath = '/judgeface/ProblemInfo'
downloadDataPath = '/judgeface/DownloadData'
tempDir = '/tmp/JDMD-OnlineJudge'
codeDirTpl = '%s/code/%d'
dataDirTpl = '%s/data/%d'

def login(loginname,password):
	conn = httplib.HTTPConnection(servername,port)
	
	params = urllib.urlencode(dict(loginname=loginname,password=password))
	headers = dict(Accept='text/html')
	conn.request("POST",loginPath, params, headers)
	
	response = conn.getresponse()
	responseHeaders = response.getheaders()
	cookie=''
	for h in responseHeaders:
		if h[0] == 'set-cookie':
			cookie = h[1]
	return cookie

def submitList(cookie):
	conn = httplib.HTTPConnection(servername,port)
	
	headers = dict(Accept='text/html',Cookie=cookie)
	conn.request("GET",submitListPath, headers=headers)
	
	response = conn.getresponse()
	print '==== status ===='
	print response.status
	
	parser = etree.XMLParser(remove_blank_text=True,strip_cdata=False)
	doc = etree.parse(response, parser=parser)
	
	result = doc.xpath('result')[0].text
	print '================= result ======================'
	print result
	
	sl = []
	if result == 'success':
		for submit in doc.getiterator('submit'):
			id = int(submit.get('id'))
			pid = submit.get('pid')
			language = submit.find('language').text
			code = submit.find('code').text
			print '================= code ========================'
			print code
			sl.append(dict(
				id=id,
				pid=pid,
				language=language,
				code=code
			))
	
	return sl

def saveCode(s):
	codeDir = codeDirTpl%(tempDir,s['id'])
	if not os.path.exists(codeDir):
		os.makedirs(codeDir)
	
	codeFilePath = '%s/main.cpp'%codeDir
	print 'codeFilePath:%s'%codeFilePath
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
	print '================== compiler return code ======='
	print p.returncode
	print '================== compiler stdout ============'
	print p.stdout.read()
	print '================== compiler stderr ============'
	print p.stderr.read()
	s['bin'] = binFilePath
	return True
	
def problemInfo(cookie,pid):
	conn = httplib.HTTPConnection(servername,port)
	
	params = urllib.urlencode(dict(pid=pid))
	headers = dict(Accept='text/html',Cookie=cookie)
	conn.request("POST",problemInfoPath, params , headers)
	
	response = conn.getresponse()
	print '==== status ===='
	print response.status
	
	parser = etree.XMLParser(remove_blank_text=True,strip_cdata=False)
	doc = etree.parse(response, parser=parser)
	
	result = doc.xpath('result')[0].text
	print '================= result ======================'
	print result
	
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
	print 'dataFilePath:%s'%dataFilePath
	f = open(dataFilePath,'w')
	f.write(response.read())
	f.close()
	
	return dataFilePath

def runTest(submit,problem,data):
	print submit
	binFilePath = submit['bin']
	inputFilePath = data['input']
	outputFilePath = '%s/%d.out'%(submit['codeDir'],data['num'])
	print outputFilePath
	errputFilePath = '%s/%d.err'%(submit['codeDir'],data['num'])
	print errputFilePath
	
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

def main():
	cookie = login('judge','123456')
	sl = submitList(cookie)
	for s in sl:
		saveCode(s)
		print s
		compileCode(s)
		pi = problemInfo(cookie,s['pid'])
		print pi
		for i in range(1,pi['dataCount'] +1 ):
			data = dict(
				num=i,
				input=downloadData(cookie,pi,i,'in'),
				output=downloadData(cookie,pi,i,'out')
			)
			runTest(s,pi,data)

main()
