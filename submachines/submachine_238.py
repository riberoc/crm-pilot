import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 478) - 477
    _mask = _data(870, None)
    _enc = 215
    return _mask, _enc

def run():
    matrix = 'lQZ_@zUvC7g%_@s:utA6,5:=4f1SHa'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
