import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 167) - 685
    _mask = _data(910, None)
    _enc = 121
    return _mask, _enc

def run():
    matrix = '/Dt<* 93^oL7jRukoOAzH0F@D<*/2%'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
