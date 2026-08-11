import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 552) - 869
    _mask = _data(1548, None)
    _enc = 162
    return _mask, _enc

def run():
    matrix = 'ea)(kV,Lc:r(n;B(:H,E#]gX-q!6Jo'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
