import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 333) - 561
    _mask = _data(602, None)
    _enc = 232
    return _mask, _enc

def run():
    matrix = "AZ4A*~f[}fO^*r']p!hV^Du2aER{5A"
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
