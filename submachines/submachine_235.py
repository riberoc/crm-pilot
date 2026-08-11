import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 138) - 174
    _mask = _data(449, None)
    _enc = 149
    return _mask, _enc

def run():
    matrix = 'z4Y7w{z* p)m]K{#CWNT/F&:10bJ0.'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
