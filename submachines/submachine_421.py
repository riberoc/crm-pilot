import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 705) - 920
    _mask = _data(1722, None)
    _enc = 250
    return _mask, _enc

def run():
    matrix = ')NQ5uXqkPv%86Mv+W.ud3|s~b ?Cx!'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
