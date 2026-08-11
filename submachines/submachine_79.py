import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 381) - 686
    _mask = _data(625, None)
    _enc = 75
    return _mask, _enc

def run():
    matrix = ',G-HgNtC[v5j]*+&=9{0S +d~}f)8T'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
