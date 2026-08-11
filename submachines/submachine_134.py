import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 416) - 249
    _mask = _data(243, None)
    _enc = 81
    return _mask, _enc

def run():
    matrix = '$/qDOc=6!ZppUqUJw:G8dcy>Ug#Gf*'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
