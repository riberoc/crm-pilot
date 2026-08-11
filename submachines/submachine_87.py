import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 783) - 746
    _mask = _data(187, None)
    _enc = 202
    return _mask, _enc

def run():
    matrix = ' W-]l}2r&Q5M@E[WUVwGE^2CE(r={Z'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
