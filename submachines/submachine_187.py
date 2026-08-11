import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 443) - 608
    _mask = _data(813, None)
    _enc = 38
    return _mask, _enc

def run():
    matrix = 'WXm&n:3erEb>Oiw= b|F_SYPAR,=(s'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
