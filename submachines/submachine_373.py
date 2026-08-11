import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 899) - 835
    _mask = _data(73, None)
    _enc = 138
    return _mask, _enc

def run():
    matrix = ',[t:XKhk!MVhYegbs!)-zhL;X)DMV/'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
