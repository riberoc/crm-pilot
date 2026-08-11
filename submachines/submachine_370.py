import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 277) - 148
    _mask = _data(486, None)
    _enc = 79
    return _mask, _enc

def run():
    matrix = '8blVX;Vz|<>eYjY$ PPHe66|_KmSbg'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
