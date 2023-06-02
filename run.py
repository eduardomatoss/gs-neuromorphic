from logging import getLogger

from app.page import load_page
from app.common.configs.startup import load_seed
from app.common.log import create_logger


create_logger()
logger = getLogger()
load_seed()

if __name__ == "__main__":
    load_page()
