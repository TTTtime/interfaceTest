import os
import sys
from common.commonTools import write_file
from common.Log import logger

filePath = ''
emailName = ''
defNameHead = 'test'
caseListName = ''
caseListFilePath = ''




class makeCase():

    def __init__(self):
        #   类与函数计数，类为key，对应value为函数数量
        self.testCaseCount = {}
        #   有效文件计数
        self.pyCaseFileCount = 0


    #   生成case的列表，写入文件
    def makeCaseList(self,fileName,defNameHead):
        try:
            #   创建caseList文件
            write_file('w',caseListFilePath,caseListName,'')
            with open(fileName,'r') as file:
                while 1:
                    #   去除每行头部的空格或制表符
                    f = file.readline().strip().strip('/t')
                    #   检查是否以class为开头
                    if f == None or f == u'\n' or f == u'' and f == u'\r\n':
                        break
                    if f.startwith('class'):
                        classNameBeg = 5
                        classNameEnd = f.find('(',1)
                        className = f[classNameBeg,classNameEnd]
                        self.testCaseCount[className] = 0
                    elif 'className'in vars() and f.startwith('def'):
                        defNameBeg = 3
                        defNameEnd = f.find('(',1)
                        defName = f[defNameBeg,defNameEnd]
                        #   过滤函数名
                        if defName.startwith(defNameHead):
                            self.testCaseCount[className] += 1
                            writeData = className + '/' + defName
                            write_file('a',caseListFilePath,caseListName,writeData)
            self.pyCaseFileCount += 1
            logger.info('获取 test case 列表结束')
        except Exception as e:
            logger.error('获取 test case 列表时异常 %s'%(e))
            return {'result':1,'msg':'获取 test case 列表时异常 %s'%(e)}
        return {'result':0,'msg':'获取 test case 列表结束','testCaseCount':self.testCaseCount}


    def start(self,filePath,defNameHead,skipDirs=None):
        try:
            for root,dirs,files in os.walk(filePath):
                if skipDirs:
                    for i in range(len(skipDirs)):
                        skipDirs[i] =  filePath + u'/' + skipDirs[i].replace('\\','/').replace('//','/')
                    root = root.replace('\\','/')
                    if root in skipDirs:
                        logger.info('跳过目录 %s'%(root))
                        continue
                if not files:
                    logger.warning('文件列表为空')
                    return {'result':1,'msg':'文件列表为空'}
                for i in files:
                    result = self.makeCaseList(i,defNameHead)
        except Exception as e:
            logger.error('处理文件时异常 %s'%(e))
            return {'result':1,'msg':'处理文件时异常 %s'%(e)}
        return {'result':0,'msg':'处理文件成功','testCaseCount':self.testCaseCount,'pyCaseFileCount':self.pyCaseFileCount}


if __name__ == '__main__':
    makeCaseIns = makeCase()
    resutl = makeCaseIns.start(filePath,defNameHead)

