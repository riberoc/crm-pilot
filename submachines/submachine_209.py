import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 367) - 462
    _mask = _data(769, None)
    _enc = 170
    return _mask, _enc

def run():
    matrix = '}}1o.|9@/# (/uq4x}n`,)q6Zotk4G'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
