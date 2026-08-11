import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 244) - 936
    _mask = _data(794, None)
    _enc = 73
    return _mask, _enc

def run():
    matrix = 'ifU-*KZD8TO-lD8 yH%<#wMObv&hdv'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
