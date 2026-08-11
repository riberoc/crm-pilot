import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 846) - 747
    _mask = _data(91, None)
    _enc = 42
    return _mask, _enc

def run():
    matrix = ' UejH/&ETByO!L!~wqFL(N/ylec,Zj'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
