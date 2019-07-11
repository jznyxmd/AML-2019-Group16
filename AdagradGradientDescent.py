class AdagradGradientDescent:
    ''' Generalized Vanilla Gradient Descent Class
        w/ AdaGrad Algo
    '''

    def __init__(self, fn_loss, fn_grad):
        self.fn_loss = fn_loss
        self.fn_grad = fn_grad
        self.eps = 1e-8
    
    def calc_velocity(self, args, cache, learning_rate, verbose=False):
        '''
        Calculate the velocity
        '''

        grad = self.fn_grad(*args)

        for i in range(len(args)):
            cache[i] += grad[i] ** 2

        velocity = []
        for i in range(len(args)):
            velocity.append(-learning_rate * grad[i] / (cache[i] + self.eps) ** 0.5)

        return velocity
    
    def find_min(self, args_init, n_max_iter, learning_rate, tol, verbose=False):
        '''
        Find the args to minimize the loss function by using the given parameters
        '''

        args = list(args_init)
        loss = self.fn_loss(*args)
        grad = self.fn_grad(*args)

        args_lst = [tuple(args)]
        loss_lst = [loss]

        cache = [0] * len(args)
        velocity = [0] * len(args)
        
        if verbose:
            print('--- init: args: {} loss: {} grad: {} ---'.format(args, loss, grad))
        
        # iterate only if the loss is greater then the given tolerance
        if abs(loss) > tol:
            for i in range(n_max_iter):

                velocity = self.calc_velocity(args, cache, learning_rate, verbose)

                for j in range(len(args)):
                    args[j] += velocity[j]

                loss = self.fn_loss(*args)

                args_lst.append(tuple(args))
                loss_lst.append(loss)

                if abs(loss) <= tol:
                    break

                if verbose:
                    print('iter: {} args: {} loss: {} velocity: {}'.format(i, args, loss, velocity))
        
        if verbose:
            print('--- final: args: {} loss: {} grad: {} ---'.format(args, loss, grad))

        return (args, args_lst, loss_lst)
