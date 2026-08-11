import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 292) - 442
    _mask = _data(898, None)
    _enc = 226
    return _mask, _enc

def run():
    matrix = '.K%0jl,`(7}:,Ie2|=CJMk$evA1dw~'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
