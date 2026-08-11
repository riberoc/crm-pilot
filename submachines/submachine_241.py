import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 705) - 637
    _mask = _data(436, None)
    _enc = 247
    return _mask, _enc

def run():
    matrix = 'I,vySz#Kb@C5!ku pckikhEm9ZyJ{#'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
