import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 151) - 578
    _mask = _data(526, None)
    _enc = 85
    return _mask, _enc

def run():
    matrix = '3M sY{d.MFPq(%FeNcI*pMw$?yTef]'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
