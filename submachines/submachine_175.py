import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 699) - 687
    _mask = _data(304, None)
    _enc = 205
    return _mask, _enc

def run():
    matrix = '],Opo2}h`ZB{?8+>vh-5&MB)i=Fya+'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
