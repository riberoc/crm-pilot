import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 647) - 903
    _mask = _data(1751, None)
    _enc = 204
    return _mask, _enc

def run():
    matrix = '9k~6Z D{G!I^o.J8h7/<|SBnblh4h1'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
