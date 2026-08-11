import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 387) - 563
    _mask = _data(676, None)
    _enc = 243
    return _mask, _enc

def run():
    matrix = 'IF.VQUl O{Kvn,Iy7qdeG{ffUR3~<h'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
