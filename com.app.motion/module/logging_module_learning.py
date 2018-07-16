import sys, logging
import os

my_logger = logging.getLogger("my_app")

# set format
formatter = logging.Formatter("%(name)s:%(asctime)s  %(levelname)-8s  %(message)s")
# file handle
log_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "mylog")
file_handler = logging.FileHandler(log_path)
file_handler.setFormatter(formatter)
# console handle
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

my_logger.setLevel(logging.DEBUG)
my_logger.addHandler(file_handler)
my_logger.addHandler(console_handler)


my_logger.debug("debug info")
my_logger.info("info log")
my_logger.warn("warn log")
my_logger.error("error log")
my_logger.error("{} service is {}".format("booking", "down"))
my_logger.fatal("fatal log")
my_logger.critical("critial log")


