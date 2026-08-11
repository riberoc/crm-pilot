import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 850) - 458
    _mask = _data(653, None)
    _enc = 1
    return _mask, _enc

def run():
    matrix = '(w|R5e4hd+`R-)m*<O+Jn85X*[1.0y'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
