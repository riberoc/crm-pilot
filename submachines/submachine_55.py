import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 203) - 670
    _mask = _data(847, None)
    _enc = 246
    return _mask, _enc

def run():
    matrix = 'PJZ{pukuLKTc^i@fk^9mEya{_GuoLx'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
