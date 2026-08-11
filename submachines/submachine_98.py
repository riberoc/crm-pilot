import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 607) - 790
    _mask = _data(1615, None)
    _enc = 243
    return _mask, _enc

def run():
    matrix = 'Rka4CAO~if=r:1y,Do;16FN]3I1AxI'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
