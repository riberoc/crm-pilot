import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 852) - 236
    _mask = _data(652, None)
    _enc = 235
    return _mask, _enc

def run():
    matrix = '1aETFRd @GDy=dNSqfO[/tTK]GIY=g'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
