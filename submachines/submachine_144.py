import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 377) - 280
    _mask = _data(895, None)
    _enc = 225
    return _mask, _enc

def run():
    matrix = 'JfK]Hf<I=.dF=B[ 88=[JG<%RmWP6u'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
