import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 121) - 446
    _mask = _data(546, None)
    _enc = 152
    return _mask, _enc

def run():
    matrix = 'g)4@w {mbKFTp]BF0>v`EhY);hp$(6'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
