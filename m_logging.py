import logging

# 方式1
logging.basicConfig(
    level=logging.DEBUG,
    filename='logger.log',
    filemode='w',
    format='%(asctime)s %(levelname)s %(message)s %(processName)s'
)

#logging.debug('debug')
#logging.info('info')
#logging.warn('warn')
#logging.error('error')
#logging.critical('critical')


# 方式2
logger = logging.getLogger()                # 可设置对象名，如果想创建多个不同的子对象，名字不能一样，否则就是同一对象 

fileh = logging.FileHandler('log2')         # 写文件
streamh = logging.StreamHandler()           # 终端输出

# 设置格式样式
formater = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

# 设置格式
fileh.setFormatter(formater)
streamh.setFormatter(formater)

# 加载
logger.addHandler(fileh)
logger.addHandler(streamh)
logger.setLevel('DEBUG')

logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')