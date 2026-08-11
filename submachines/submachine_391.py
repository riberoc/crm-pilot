import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 490) - 586
    _mask = _data(849, None)
    _enc = 116
    return _mask, _enc

def run():
    matrix = '(SoAS FqA)Q#]IrI3|V8|-9j{|Hdp7'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
