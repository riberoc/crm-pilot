import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 426) - 645
    _mask = _data(659, None)
    _enc = 163
    return _mask, _enc

def run():
    matrix = '3.rC[Rc&49&hM%{n0QZ{!,* 3ZZ0~R'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
