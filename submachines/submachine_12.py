import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 293) - 266
    _mask = _data(230, None)
    _enc = 178
    return _mask, _enc

def run():
    matrix = '2r{2Pqda1jXt.CUaK-~e)^lD5|iN,b'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
