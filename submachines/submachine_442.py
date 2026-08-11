import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 598) - 827
    _mask = _data(482, None)
    _enc = 97
    return _mask, _enc

def run():
    matrix = '!|P=?iD*K1?luZE*[wJ-~bubm3{gl;'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
