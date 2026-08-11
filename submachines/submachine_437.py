import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 548) - 436
    _mask = _data(1019, None)
    _enc = 50
    return _mask, _enc

def run():
    matrix = ',g`_VkC$t~UnJ=(jivuA3A7Mf _L3K'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
