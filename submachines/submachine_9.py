import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 661) - 236
    _mask = _data(1017, None)
    _enc = 150
    return _mask, _enc

def run():
    matrix = '1#%h@)bT<XYRm@+j6@nSr9 ie)101B'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
