
import os






moduleDict = {
    1:'h'
}


class MakeCase():



    def __init__(self):
        pass


    def makeStart(self,apiType):
        if apiType == 'rest':
            part1 = '''
                import json
                import unittest2
                import requests
            '''
            part2 = '''
            class %s(unittest2.TestCase):
            '''%()
            part3 = '''
            @classmethod
            '''
            part4 = '''
            '''
            part5 = '''
            '''
            part6 = '''
            '''
            part7 = '''
            '''
            part8 = '''
            '''
            part9 = '''
            '''
            part10 = '''
            '''
        elif apiType == 'xmlrpc':
            pass

    def restApiCase(self):
        pass



    def xmlrpcApiCase(self):
        pass

#@paramunittest.parametrized(*login_xls)
class test_wt(unittest2.TestCase):

    def setParameters(self, case_name, path, query, method):
        pass
        """
        set params
        :param case_name:
        :param path
        :param query
        :param method
        :return:
        """
        #self.case_name = str(case_name)
        #self.path = str(path)
        #self.query = str(query)
        #self.method = str(method)
        self.case_name = 'testHEHEHE000'

    def description(self):
        """
        test report description
        :return:
        """
        #self.case_name
        pass
    @classmethod
    def setUp(self):
        """

        :return:
        """
        self.case_name = 'testHEHEHE000'
        pass
        #print(self.case_name+"测试开始前准备")

    def test01case(self):
        url = 'http://172.16.230.206:8080/evsserver/base/BaseUserService/GET/Users'
        method = 'post'
        data = {"loginName":"wt"}
        self.checkResult(method,url,data)

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self,method,url,data):# 断言
        """
        check test result
        :return:
        """
        #url1 = "http://www.xxx.com/login?"
        #new_url = url1 + self.query
        #data = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))# 将一个完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}
        #info = RunMain().run_main(method,url,data)# 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        header = {'Content-Type':'application/json'}
        json_data = json.dumps(data)
        result = requests.post(url,data=json_data,headers=header,timeout=60)
        result = json.loads(result.text)['para'][0]['departmentId']
        print(result['para'][0]['departmentId'])