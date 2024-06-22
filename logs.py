import logging
import os

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("Augusto", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s %(lineno)s %(filename)s %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)

# exemplo de uso
try:
    1/0
except ZeroDivisionError as e:
    log.error("%s", str(e))

