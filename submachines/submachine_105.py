import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 523) - 958
    _mask = _data(1539, None)
    _enc = 67
    return _mask, _enc

def run():
    matrix = 'FqM`]eX2vb$~E:LA%Y#-EN`kwmUD5j'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
