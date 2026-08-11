import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 773) - 472
    _mask = _data(369, None)
    _enc = 157
    return _mask, _enc

def run():
    matrix = 'U /^9ci0?zl=?`}Ao`Q94mM6mn6GP%'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
