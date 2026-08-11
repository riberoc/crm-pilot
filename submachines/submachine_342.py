import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 161) - 925
    _mask = _data(1237, None)
    _enc = 194
    return _mask, _enc

def run():
    matrix = '8um2U%p^Db,O2h:zK~i|8 iI],K2(,'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
