import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 813) - 624
    _mask = _data(40, None)
    _enc = 135
    return _mask, _enc

def run():
    matrix = '<@wqxvZ,F]s7X|,u)nEqGM32o}2Gm6'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
