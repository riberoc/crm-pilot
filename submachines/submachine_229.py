import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 169) - 483
    _mask = _data(696, None)
    _enc = 50
    return _mask, _enc

def run():
    matrix = 'd%w.DF`E1nEwK(_nrGpvF[^I.^^o I'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
