import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 514) - 149
    _mask = _data(888, None)
    _enc = 243
    return _mask, _enc

def run():
    matrix = 'CCxiHN7JMbfNWiC(TvQ}/M t=W9yY$'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
