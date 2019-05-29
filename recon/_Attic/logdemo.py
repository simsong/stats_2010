# Demo to create my own log handler

import logging

class DFXMLHandler(logging.Handler):
    def emit(self,record):
        print("===")

dh = DFXMLHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
dh.setFormatter(dh)
logger = logging.getLogger('demo')
logger.setLevel(logging.INFO)
logger.addHandler(dh)
logger.info('a test at info')
logger.warn('a test at warn')
