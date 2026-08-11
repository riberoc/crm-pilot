import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 226) - 200
    _mask = _data(337, None)
    _enc = 237
    return _mask, _enc

def run():
    matrix = '-M-BP+ u;Yl}e}FAyOL@8*IkoPjPi<'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
