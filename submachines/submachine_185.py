import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 900) - 408
    _mask = _data(437, None)
    _enc = 138
    return _mask, _enc

def run():
    matrix = '(~;LP6svV;Q?Ga63Ml( :H-x$Ki[lg'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
