import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 731) - 743
    _mask = _data(410, None)
    _enc = 64
    return _mask, _enc

def run():
    matrix = 'jR5vj!1*y3mktuIuAl:jbe-MUP uvT'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
