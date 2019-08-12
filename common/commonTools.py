import codecs
import os
from common.Log import logger
import datetime


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