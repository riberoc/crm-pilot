import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 786) - 366
    _mask = _data(310, None)
    _enc = 174
    return _mask, _enc

def run():
    matrix = '!{gVA!4QqP.%)IDb3d]Pum1[IEr8Bj'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
