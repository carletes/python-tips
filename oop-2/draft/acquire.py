import satellites


data_sources = [
    satellites.MetOp("MetOp-A"),
    satellites.MetOp("MetOp-B"),
]

for s in data_sources:
    s.acquire()
