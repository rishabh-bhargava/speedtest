from loguru import logger
import speedtest

logger.add("speedtest_results.log", format="{message}", rotation="1 hour")

# params
servers = []
threads = 1

while True:
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
