import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 348) - 622
    _mask = _data(964, None)
    _enc = 36
    return _mask, _enc

def run():
    matrix = 'SaXz$#PO;kF98J voHL7(n#K[hh#hZ'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
