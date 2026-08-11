import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 475) - 315
    _mask = _data(40, None)
    _enc = 179
    return _mask, _enc

def run():
    matrix = ',t#@yxxvT93 0%1`wc9Hz(qG;pJT$D'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
