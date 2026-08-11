import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 349) - 502
    _mask = _data(869, None)
    _enc = 78
    return _mask, _enc

def run():
    matrix = 'aTpn/)dmVFl#eIydfFdd0WG<D45LsA'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
