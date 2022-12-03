import logging
import sys


logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('logfile.log', mode='a', encoding='utf-8')
handler.setLevel(logging.DEBUG)
handler_err = logging.StreamHandler(stream=sys.stderr)
handler_err.setLevel(logging.ERROR)

format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(format)
handler_err.setFormatter(format)

logger.addHandler(handler)
logger.addHandler(handler_err)
