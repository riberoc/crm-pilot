import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 481) - 897
    _mask = _data(1506, None)
    _enc = 144
    return _mask, _enc

def run():
    matrix = 'q7)XOE~-qw(*8rxL%Br44GB_>=^qW%'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
