import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 601) - 880
    _mask = _data(402, None)
    _enc = 87
    return _mask, _enc

def run():
    matrix = ';Z]z*Zw:~+*nr.KuKyD:+G:at0d0UC'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
