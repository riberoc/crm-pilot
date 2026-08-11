import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 513) - 901
    _mask = _data(1662, None)
    _enc = 251
    return _mask, _enc

def run():
    matrix = 'A b/3A{ZR=Uoy.F-b)[[?)rg}ggsQ5'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
