import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 584) - 718
    _mask = _data(316, None)
    _enc = 167
    return _mask, _enc

def run():
    matrix = ', Rg2jCA/.t-2cT]Fkw%~j>qy:13+{'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
