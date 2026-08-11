import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 465) - 697
    _mask = _data(657, None)
    _enc = 149
    return _mask, _enc

def run():
    matrix = 'Z+Ue([6dw)F9I;y2@2 :Ny&^Cp(G>Q'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
