import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 381) - 508
    _mask = _data(1015, None)
    _enc = 139
    return _mask, _enc

def run():
    matrix = 'tHK1} M#GnUqJ^IJXjWGX#K8YW-MWV'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
