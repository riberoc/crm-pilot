import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 689) - 329
    _mask = _data(169, None)
    _enc = 223
    return _mask, _enc

def run():
    matrix = 'RMcZ!GtMRP>Jf6A| &{|sff#,wr{(W'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
