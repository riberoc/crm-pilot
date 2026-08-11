import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 124) - 326
    _mask = _data(429, None)
    _enc = 133
    return _mask, _enc

def run():
    matrix = '1+2DN+mt(an(ix B}W-*Fv3,r)9|pz'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
