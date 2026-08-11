import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 122) - 746
    _mask = _data(985, None)
    _enc = 185
    return _mask, _enc

def run():
    matrix = ' EzljZJ,FFiVD]?M2@,U/;n]YuQ;/N'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
