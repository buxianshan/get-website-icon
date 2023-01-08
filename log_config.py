import logging
from loguru import logger
import platform


# create a custom handler
class InterceptHandler(logging.Handler):
    def emit(self, record):
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log("DEBUG", record.getMessage())


logger.add("icon-server.log")
logging.basicConfig(handlers=[InterceptHandler()], level='INFO')

# 如果是linux系统，则日志不记录基本的请求响应信息
if platform.system() == "Linux":
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.WARNING)

