import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 239) - 230
    _mask = _data(387, None)
    _enc = 156
    return _mask, _enc

def run():
    matrix = '!]%8Xz2Img)H>#m*S8)1Q<^Bv? S@|'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
