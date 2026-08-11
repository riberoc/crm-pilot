import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 445) - 281
    _mask = _data(92, None)
    _enc = 212
    return _mask, _enc

def run():
    matrix = 'J>2H:y,?q]6]9X+jtRxT{Ity#Zih H'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
