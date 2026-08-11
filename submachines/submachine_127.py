import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 974) - 610
    _mask = _data(229, None)
    _enc = 192
    return _mask, _enc

def run():
    matrix = 'H}i}%L0IJ [o;Og*F61`=Oj]xB~b^z'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
