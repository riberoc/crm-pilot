import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 346) - 569
    _mask = _data(981, None)
    _enc = 91
    return _mask, _enc

def run():
    matrix = 'VbsQL)nY%)m`Y UJV[&}%Lb)}51N<{'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
