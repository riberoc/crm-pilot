import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 847) - 310
    _mask = _data(350, None)
    _enc = 195
    return _mask, _enc

def run():
    matrix = 'ot7_#E,x8#cNW<V;F7$T}K+H y+>$+'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
