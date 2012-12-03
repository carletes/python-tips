import logging

import satellites


data_sources = [
    satellites.NOAA("NOA-18"),
    satellites.NOAA("NOA-19"),
    satellites.MetOp("MetOp-A"),
    satellites.MetOp("MetOp-B"),
]

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(name)s %(message)s")

for s in data_sources:
    print s.acquire()
