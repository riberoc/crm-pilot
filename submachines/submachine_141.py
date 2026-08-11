import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 960) - 784
    _mask = _data(102, None)
    _enc = 144
    return _mask, _enc

def run():
    matrix = 'tBh40, <SR1}1-R-cMA,`HT~UB(G!u'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
