import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 473) - 684
    _mask = _data(820, None)
    _enc = 72
    return _mask, _enc

def run():
    matrix = '~[,seeX3,hpa4VX8S6dfwECLos}Pie'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
