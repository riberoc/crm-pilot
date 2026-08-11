import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 818) - 161
    _mask = _data(1008, None)
    _enc = 43
    return _mask, _enc

def run():
    matrix = '^OEBL]%?PL Q5HssDN@Oh:u;NjQNt<'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
