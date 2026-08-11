import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 615) - 128
    _mask = _data(808, None)
    _enc = 192
    return _mask, _enc

def run():
    matrix = '/4XN#9AIeb6:H!l ;;i]O[Hi7vfvu?'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
