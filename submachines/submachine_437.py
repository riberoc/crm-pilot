import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 931) - 944
    _mask = _data(107, None)
    _enc = 19
    return _mask, _enc

def run():
    matrix = 'XUBIXMFL)]o +%u&_ArzOEX[f5Y%X7'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
