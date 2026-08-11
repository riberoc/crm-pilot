import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 811) - 640
    _mask = _data(475, None)
    _enc = 115
    return _mask, _enc

def run():
    matrix = 'RgY *ORg!DM)nMGZ2z(]DK]?JDdCF&'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
