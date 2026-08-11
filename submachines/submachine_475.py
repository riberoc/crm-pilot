import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 630) - 788
    _mask = _data(351, None)
    _enc = 2
    return _mask, _enc

def run():
    matrix = 'Xhv~tY;g[3K*PS]O%E7>XP{ |MQmf+'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
