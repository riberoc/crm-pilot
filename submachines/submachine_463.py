import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 130) - 464
    _mask = _data(681, None)
    _enc = 77
    return _mask, _enc

def run():
    matrix = 'UHecROER-DXDcCbA6o/MmA ]V4^ha5'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
