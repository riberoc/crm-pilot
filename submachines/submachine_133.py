import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 906) - 855
    _mask = _data(1929, None)
    _enc = 190
    return _mask, _enc

def run():
    matrix = 'N.gghaVeO%@3|j&(+T {E-I)pSw%c_'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
