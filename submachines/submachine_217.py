import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 743) - 607
    _mask = _data(472, None)
    _enc = 248
    return _mask, _enc

def run():
    matrix = ';i0x,>~?WMpto@a;`5S7q8j~ q.o#B'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
