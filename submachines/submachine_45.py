import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 997) - 909
    _mask = _data(1890, None)
    _enc = 238
    return _mask, _enc

def run():
    matrix = 'Jq.b[!5,8&*J~vM66_5n n7X;g@T:`'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
