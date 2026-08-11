import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 639) - 204
    _mask = _data(669, None)
    _enc = 24
    return _mask, _enc

def run():
    matrix = 'B:9PSK3cCU>&|e DJlt@Y11d8~8B|M'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
