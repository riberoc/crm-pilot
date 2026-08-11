import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 612) - 764
    _mask = _data(474, None)
    _enc = 201
    return _mask, _enc

def run():
    matrix = 'c_^2mz&yMcO =k+wlf9Ovz)Cp9&wgb'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
