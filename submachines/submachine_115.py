import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 646) - 727
    _mask = _data(268, None)
    _enc = 180
    return _mask, _enc

def run():
    matrix = 'HZ2Ikx; 8h-ZWYRw|t_cXhsTFSNiVR'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
