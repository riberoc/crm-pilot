import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 869) - 276
    _mask = _data(681, None)
    _enc = 182
    return _mask, _enc

def run():
    matrix = 'aBV-fIw~#;&)e, |v1W*)EPQNMpI:X'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
