import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 286) - 923
    _mask = _data(1386, None)
    _enc = 213
    return _mask, _enc

def run():
    matrix = 'NoBWBI-F%2Vh +L`Ed{tb~^@v=>Oh9'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
