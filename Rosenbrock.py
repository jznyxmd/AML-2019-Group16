def find_partial_derivatives():
    '''
    Find the symbolic form of the partial_derivatives of
    the Rosenbrock function
    '''

    # require sympy package
    import sympy

    a, b, x, y = sympy.symbols('a b x y')

    f = (a - x) ** 2 + b * (y - x ** 2) ** 2

    df_dx = sympy.diff(f, x)
    df_dy = sympy.diff(f, y)

    print('df/dx: {}'.format(df_dx))
    print('df/dy: {}'.format(df_dy))


def generate_fn(a, b):
    '''
    Generate Rosenbrock function and its derivative functions
    by the given parameters
    '''

    def fn(x, y):
        '''
        The Rosenbrock function
        '''
        return (a - x) ** 2 + b * (y - x ** 2) ** 2


    def fn_d(x, y):
        '''
        The derivatives of the Rosenbrock function
        '''
        df_dx = -2 * a - 4 * b * x * (-x ** 2 + y) + 2 * x
        df_dy = b * (-2 * x ** 2 + 2 * y)
        return (df_dx, df_dy)
    
    return fn, fn_d
