import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 668) - 525
    _mask = _data(49, None)
    _enc = 170
    return _mask, _enc

def run():
    matrix = 'dWAOuw}Rs. pX9K*7RhaXbbU!~14AG'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
