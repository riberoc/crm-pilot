import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 810) - 753
    _mask = _data(205, None)
    _enc = 230
    return _mask, _enc

def run():
    matrix = 'I,vVb*5%h_},eF+)T%^(V91T!Ny@5F'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
