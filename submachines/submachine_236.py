import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 508) - 214
    _mask = _data(167, None)
    _enc = 128
    return _mask, _enc

def run():
    matrix = 'D8Q5? 7G>^<PVA|)({>pLG;C]5bdo|'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
