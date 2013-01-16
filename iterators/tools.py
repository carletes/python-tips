"""Helper tools."""

import resource


__all__ = [
    "memory_usage",
]


class memory_usage():
    """Context manager that keeps track of the memory used by a Python code
    fragment.

    """
    def __init__(self):
        self.initial_rss = 0
        self.final_rss = 0

    def __enter__(self):
        self.initial_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        return self

    def __exit__(self, *exc_info):
        self.final_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    @property
    def rss(self):
        """RSS memory delta.

        """
        return self.final_rss - self.initial_rss
