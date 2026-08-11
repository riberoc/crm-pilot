import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 425) - 105
    _mask = _data(299, None)
    _enc = 23
    return _mask, _enc

def run():
    matrix = 'ptXg4pf9]r~;Qh ^~:(]PG3-K#$^Q)'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
