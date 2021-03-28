from datetime import datetime
from loguru import logger
import speedtest
import time

logger.add("speedtest_results.log", format="{message}", rotation="1 hour")

# params
servers = []
threads = 1

while True:
    try:
        s = speedtest.Speedtest()
        s.get_servers(servers)
        s.get_best_server()
        s.download(threads=threads)
        s.upload(threads=threads)
        s.results.share()

        results_dict = s.results.dict()
        logger.info(
            '{}|{}|{}',
            results_dict['timestamp'],
            results_dict['download'],
            results_dict['upload']
        )
    except (speedtest.ShareResultsConnectFailure, speedtest.ConfigRetrievalError):
        timestamp_now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        logger.info('{}|{}|{}', timestamp_now, 0, 0)
        time.sleep(5)
