import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 320) - 136
    _mask = _data(75, None)
    _enc = 151
    return _mask, _enc

def run():
    matrix = 'MkfLg1pQDp)/.KA/jxi/d0*2IB-2u;'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
