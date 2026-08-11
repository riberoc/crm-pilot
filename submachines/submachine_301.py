import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 349) - 521
    _mask = _data(884, None)
    _enc = 37
    return _mask, _enc

def run():
    matrix = '=S~Z] 7xBr5EWJ3*x3#cr<@uWF42%a'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
