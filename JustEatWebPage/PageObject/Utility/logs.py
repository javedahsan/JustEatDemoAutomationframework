import logging
import os
import env
Log_dir = env.Log_dir

class Log(object):
    def __init__(self):
        self.debug = logging.DEBUG
        self.info = logging.INFO
        self.error = logging.ERROR
        self.critical = logging.CRITICAL
        self.warning = logging.WARNING
        self.notset = logging.NOTSET
        self.directory = Log_dir

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def logConfig(self, logLevel):
        print('LogFile:', self.directory + 'test.log')
        logging.basicConfig(filename=self.directory + 'test.log', level=self.__getattribute__(logLevel), format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')

    def loging(self, msg, logLevel):
        self.logConfig(logLevel)

        if (logLevel == "debug"):
            logging.debug(msg)
        elif logLevel == "info":
            logging.info(msg)
        elif logLevel == "error":
            logging.error(msg)
        elif logLevel == "warning":
            logging.warning(msg)
        elif logLevel == "critical":
            logging.critical(msg)
        else:
            logging.notset(msg)

if __name__ == "__main__":
    log = Log()

    msg = "Testing Debug"
    log.loging(msg, "debug")
    msg = "Testing Info"
    log.loging(msg, "info")
    msg = "Testing Error"
    log.loging(msg, "error")
    msg = "Testing critical"
    log.loging(msg, "critical")
    msg = "Testing warning"
    log.loging(msg, "warning")
