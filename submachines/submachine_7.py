import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 906) - 512
    _mask = _data(497, None)
    _enc = 103
    return _mask, _enc

def run():
    matrix = ':sl3n@(Ou3jMt@>tCuXSg#r4SR*u _'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
