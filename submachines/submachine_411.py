import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 850) - 824
    _mask = _data(1870, None)
    _enc = 246
    return _mask, _enc

def run():
    matrix = '9r~7w8h:^lnqWL-`yB f*:{u6`Vss4'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
