import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 572) - 744
    _mask = _data(438, None)
    _enc = 177
    return _mask, _enc

def run():
    matrix = 'RLbwzMdR,Np%[_#<+%-iox5mu)H#(i'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
