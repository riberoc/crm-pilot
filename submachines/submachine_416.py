import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 236) - 627
    _mask = _data(588, None)
    _enc = 38
    return _mask, _enc

def run():
    matrix = 'jm/Ys!Kd_!N u@}}Mwd`10T,|B?B&a'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
