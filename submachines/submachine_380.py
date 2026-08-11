import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 894) - 515
    _mask = _data(437, None)
    _enc = 192
    return _mask, _enc

def run():
    matrix = '53p[]b[, (7Q83j`*p$c[e]Hh>83`A'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
