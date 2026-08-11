import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 450) - 521
    _mask = _data(869, None)
    _enc = 158
    return _mask, _enc

def run():
    matrix = ' N!yE5+/5YNpkXBz49A&u6rWrJQ#2e'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
