import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 168) - 163
    _mask = _data(452, None)
    _enc = 200
    return _mask, _enc

def run():
    matrix = '# gAmV[ni7urok(*}z}i+&H8=ZV7|r'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
