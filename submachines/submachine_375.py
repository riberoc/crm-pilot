import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 363) - 775
    _mask = _data(529, None)
    _enc = 117
    return _mask, _enc

def run():
    matrix = 'vVSY1p ^q}CI@vGk5W1ElVcSRQYClQ'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
