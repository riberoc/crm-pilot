import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 634) - 615
    _mask = _data(180, None)
    _enc = 101
    return _mask, _enc

def run():
    matrix = 'nu ZqB<k6Aj>Z#Xl]$c+<gE,2Z,:]_'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
