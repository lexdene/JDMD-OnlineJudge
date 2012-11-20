# -*- coding: utf-8 -*-

import subprocess
from JudgerBase import JudgerBase

class Gcc(JudgerBase):
	def compile(self,s):
		binFilePath = '%s/bin'%s['codeDir']
		p = subprocess.Popen(
			["g++",'-o',binFilePath,'-pipe','-O2','-Wall','-W','-DONLINE_JUDGE',s['codeFilePath'] ],
			stdout = subprocess.PIPE,
			stderr = subprocess.PIPE,
		)
		p.wait()
		compileErrorMessage = p.stderr.read(1024*8)
		s['bin'] = binFilePath
		
		compileResult = dict()
		if p.returncode != 0:
			compileResult['result'] = 'compile error'
		
		if compileErrorMessage:
			compileResult['compile message'] = compileErrorMessage
		
		return compileResult
