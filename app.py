import logging
logging.basicConfig(format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
                    level=logging.INFO, filename='default.log', filemode='a')

import database


if __name__ == "__main__":
    logging.info('Hello, log!')
