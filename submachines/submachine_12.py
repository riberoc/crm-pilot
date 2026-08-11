import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 786) - 825
    _mask = _data(78, None)
    _enc = 54
    return _mask, _enc

def run():
    matrix = '5Y`06~<MGW;!W0UN*Jqto ?XP%XagR'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
