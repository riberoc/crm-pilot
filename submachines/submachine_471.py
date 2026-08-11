import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 408) - 405
    _mask = _data(983, None)
    _enc = 178
    return _mask, _enc

def run():
    matrix = 'I1xj#0;O x,ISoQ2$y{UZ1&Eau~DZD'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
