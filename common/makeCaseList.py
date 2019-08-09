import os
import sys
import commonTools


filePath = ''
emailName = ''
defNameHead = 'test'

caseListName = ''
caseListFilePath = ''


#   生成case的列表，写入文件
def makeCaseList():
    #   类与函数计数，类为key，对应value为函数数量
    testCaseCount = {}
    #   有效文件计数
    pyCaseFileCount = 0
    def makeCaseList1(fileName,defNameHead):
        nonlocal testCaseCount,pyCaseFileCount
        try:
            #   创建caseList文件
            commonTools.write_file('w',caseListFilePath,caseListName,'')
            with open(fileName,'r') as file:
                while 1:
                    #   去除每行头部的空格或制表符
                    f = file.readline().strip().strip('/t')
                    #   检查是否以class为开头
                    if file_data == None or file_data == u'\n' or file_data == u'' and file_data == u'\r\n':
                        break
                    if f.startwith('class'):
                        classNameBeg = 5
                        classNameEnd = f.find('(',1)
                        className = f[classNameBeg,classNameEnd]
                        testCaseCount[className] = 0
                        classCount += 1
                    elif 'className'in vars() and f.startwith('def'):
                        defNameBeg = 3
                        defNameEnd = f.find('(',1)
                        defName = f[defNameBeg,defNameEnd]
                        #   过滤函数名
                        if defName.startwith(defNameHead):
                            defCount += 1
                            testCaseCount[className] += 1
                            writeData = className + '/' + defName
                            commonTools.write_file('a',caseListFilePath,caseListName,writeData)
            pyCaseFileCount += 1
            commonTools.logging.info('获取 test case 列表结束，文件共 %s ,类 %s ，函数 %s'%(pyCaseFileCount,classCount,defCount))
        except Exception as e:
            commonTools.logging.error('获取 test case 列表时异常 %s'%(e))
            return {'result':1,'msg':'获取 test case 列表时异常 %s'%(e)}
        return {'result':0,'msg':'获取 test case 列表结束，文件共 %s ,类 %s ，函数 %s'%(pyCaseFileCount,classCount,defCount),''}
    return makeCaseList1


def start(filePath,skipDirs,defNameHead):
    try:
        for root,dirs,files in os.walk(file_path):
            for i in range(len(skip_dir)):
                skip_dir[i] =  file_path + u'/' + skip_dir[i].replace('\\','/').replace('//','/')
            root = root.replace('\\','/')
            if root in skip_dir:
                commonTools.logging.info('跳过目录 %s'%(root))
                continue
            if not files:
                commonTools.logger.warning('文件列表为空')
                return {'result':1,'msg':'文件列表为空'}
            for i in files:
                makeCaseList(i,defNameHead)
    except Exception as e:
        commonTools.logging.error('处理文件时异常 %s'%(e))
        return {'result':1,'msg':'处理文件时异常 %s'%(e)}
    return {'result':0,'msg':'处理文件成功'}


if __name__ == '__main__':
    start(filePath,defNameHead)

