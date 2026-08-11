import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 894) - 277
    _mask = _data(529, None)
    _enc = 89
    return _mask, _enc

def run():
    matrix = '@5UhJcTBO;|nZHt_Vw_7-].gahZc@b'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
