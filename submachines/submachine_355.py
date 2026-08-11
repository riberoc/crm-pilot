import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 363) - 556
    _mask = _data(918, None)
    _enc = 218
    return _mask, _enc

def run():
    matrix = '5,y]$sPvue0hX`Csw&w%rl^H(SU0zq'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
