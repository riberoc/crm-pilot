import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 818) - 180
    _mask = _data(535, None)
    _enc = 103
    return _mask, _enc

def run():
    matrix = '83!#k&v.cAKoHibi%02Qlp A~H0MEl'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
