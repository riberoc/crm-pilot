import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 473) - 311
    _mask = _data(87, None)
    _enc = 80
    return _mask, _enc

def run():
    matrix = '[)T`ael CiM+R<h++Bz%h/n1T/rUzf'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
