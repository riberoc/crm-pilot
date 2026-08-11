import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 936) - 585
    _mask = _data(180, None)
    _enc = 222
    return _mask, _enc

def run():
    matrix = '^`2=8GT=1G_9Te*aN~0jE|xT6EQftw'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
