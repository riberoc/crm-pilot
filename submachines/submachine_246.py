import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 847) - 899
    _mask = _data(1903, None)
    _enc = 153
    return _mask, _enc

def run():
    matrix = 'gF)Q OJC]t]6Zm#>=K`S<4Q<@2mYL8'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
