import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 643) - 955
    _mask = _data(365, None)
    _enc = 39
    return _mask, _enc

def run():
    matrix = 'KX)=j[H`Th*``q0ie{x} k+^lY+S%p'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
