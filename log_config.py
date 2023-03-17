import logging
from loguru import logger
import platform
import os


# create a custom handler
class InterceptHandler(logging.Handler):
    def emit(self, record):
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log("DEBUG", record.getMessage())


ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
logger.add(f"{ROOT_PATH}/server.log")
logging.basicConfig(handlers=[InterceptHandler()], level='INFO')

# 如果是linux系统，则日志不记录基本的请求响应信息
if platform.system() == "Linux":
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.WARNING)

