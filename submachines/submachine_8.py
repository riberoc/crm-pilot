import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 475) - 746
    _mask = _data(644, None)
    _enc = 108
    return _mask, _enc

def run():
    matrix = 'WAtNt^UM(puU#-#F{Vq232!LntQK^{'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
