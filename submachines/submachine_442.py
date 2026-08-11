import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 554) - 350
    _mask = _data(900, None)
    _enc = 84
    return _mask, _enc

def run():
    matrix = 'V;v; P-{.S4B}9od@}xLg=%_&G<gh)'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
