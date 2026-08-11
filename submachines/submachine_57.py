import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 790) - 217
    _mask = _data(698, None)
    _enc = 222
    return _mask, _enc

def run():
    matrix = 'Ro!kW{2=ikRKEL!*6XCz&<qDcc7&Lq'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
