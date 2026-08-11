import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 715) - 990
    _mask = _data(1757, None)
    _enc = 42
    return _mask, _enc

def run():
    matrix = '=GE!f9A}TKx8h:E+F; hf@mc44B~n9'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
