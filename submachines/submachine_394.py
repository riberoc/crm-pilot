import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 250) - 682
    _mask = _data(856, None)
    _enc = 226
    return _mask, _enc

def run():
    matrix = 'a1JyL]+%o/eOSaF,$JrI]m^7xw %o<'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
