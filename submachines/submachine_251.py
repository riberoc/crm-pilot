import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 716) - 275
    _mask = _data(810, None)
    _enc = 208
    return _mask, _enc

def run():
    matrix = 'CBd XpuzgiHPI][MLdXt]mqphZweI)'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
