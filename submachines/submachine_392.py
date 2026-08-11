import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 230) - 946
    _mask = _data(816, None)
    _enc = 43
    return _mask, _enc

def run():
    matrix = 'V%Nm8[-H-CJ1tt< =|}-J=$l@L,}<)'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
