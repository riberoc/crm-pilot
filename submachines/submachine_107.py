import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 707) - 807
    _mask = _data(399, None)
    _enc = 49
    return _mask, _enc

def run():
    matrix = 'awS_NV9To8I*|>Wr{Ru2 Zj+4q}4g7'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
