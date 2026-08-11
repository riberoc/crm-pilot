import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 647) - 674
    _mask = _data(120, None)
    _enc = 64
    return _mask, _enc

def run():
    matrix = '*Z<r607z}|!n(hu;0#5690(N{?YJE '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
