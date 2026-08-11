import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 395) - 974
    _mask = _data(1447, None)
    _enc = 80
    return _mask, _enc

def run():
    matrix = 'O:h<@s,l[i2oX9 =Rn38[:;*1d1ix4'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
