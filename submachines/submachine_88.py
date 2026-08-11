import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 439) - 653
    _mask = _data(750, None)
    _enc = 195
    return _mask, _enc

def run():
    matrix = 'W_gvh/VQzhCwYG0 zAS=Zy2BCCsCVg'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
