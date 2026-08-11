import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 752) - 839
    _mask = _data(401, None)
    _enc = 28
    return _mask, _enc

def run():
    matrix = '>T8>zX iniPnaG:2js4POCXlYU@SZD'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
