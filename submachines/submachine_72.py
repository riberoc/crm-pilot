import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 990) - 112
    _mask = _data(837, None)
    _enc = 40
    return _mask, _enc

def run():
    matrix = 'zBi )._Y6W77B^6v-=LeMWNh/,.7b['
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
