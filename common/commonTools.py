import codecs
import os
from logging.handlers import RotatingFileHandler
import logging

argv0_list = sys.argv[0].split("\\")
script_name = argv0_list[-1][0:-3]
script_name = script_name.replace('.','')
#base_dir = os.path.join(os.path.dirname(__file__),'../../logs')
base_dir = os.path.join(os.path.dirname(__file__),'D:/python3/logs')
log_file = os.path.join(base_dir,'%s.log'%script_name)
#def get_logger(log_dir):
'''
fh = logging.FileHandler(log_dir,encoding='utf-8') #创建一个文件流并设置编码utf8
logger = logging.getLogger() #获得一个logger对象，默认是root
logger.setLevel(logging.DEBUG)  #设置最低等级debug
fm = logging.Formatter("%(asctime)s --- %(message)s")  #设置日志格式
logger.addHandler(fh) #把文件流添加进来，流向写入到文件
fh.setFormatter(fm) #把文件流添加写入格式
logger = logging.getLogger()
'''
logger = logging.getLogger() #定义对应的程序模块名name，默认是root
logger.setLevel(logging.INFO) #指定最低的日志级别
ch = logging.StreamHandler() #创建日志输出到屏幕控制台的handler
ch.setLevel(logging.INFO) #设置日志等级

#fh = logging.FileHandler(log_file)#创建向文件access.log输出日志信息的handler
#fh.setLevel(logging.INFO) #设置输出到文件最低日志级别

Rthandler = RotatingFileHandler(log_file, mode='a', maxBytes= 50 * 1024 * 1024, backupCount = 10)
Rthandler.setLevel(logging.INFO)
#create formatter
#formatter = logging.Formatter('%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s') #定义日志输出格式
formatter = logging.Formatter('[%(asctime)s] [%(filename)s] [%(levelname)s] [line:%(lineno)d]:%(message)s')
#add formatter to ch and fh
ch.setFormatter(formatter) #选择一个格式
#fh.setFormatter(formatter)
Rthandler.setFormatter(formatter)

logger.addHandler(ch) #增加指定的handler
#logger.addHandler(fh)
logger.addHandler(Rthandler)


def write_file(open_method,file_dir,file_name,write_info):
    #   写入方法（w创建写入a追加写入），文件名，写入信息（分隔符换行等信息由调入者格式化传入）
    file_name = file_name.replace(':', '-')
    file = ''.join([file_dir, os.sep, file_name])
    file = file.replace('\\', '/')
    try:
        if (open_method == 'a' and os.path.exists(file))  or open_method == 'w':
            with codecs.open(file,open_method,'gb18030') as f:
                #   判断写入信息是否为空，非空则写入
                if write_info.strip():
                    f.write(write_info)
        elif open_method not in ['w','a']:
            print(u'========== open_method error : %s %s=========='%(open_method,datetime.datetime.now()))
            return {'result':'1','info':'open_method error'}
        elif os.path.exists(file) == False:
            logger.info(u'file not exist : %s '%(file))
            return {'result':'1','info':'file not exist'}
    except Exception as e:
        logger.info(u'file write error : %s '%(e))
        return {'result':'1','info':'file write error : %s'%e}
    return {'result':'0','info':'file write success','file_name':file_name}