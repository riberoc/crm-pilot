import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 228) - 460
    _mask = _data(314, None)
    _enc = 31
    return _mask, _enc

def run():
    matrix = 'J?v3izzOOF2sS `Q2_v15gA;@w!=Iz'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
