class NesterovGradientDescent:
    ''' Generalized Vanilla Gradient Descent Class
        w/ Nesterov Optimization
    '''

    def __init__(self, fn_loss, fn_grad):
        self.fn_loss = fn_loss
        self.fn_grad = fn_grad
    
    def calc_velocity(self, args, velocity_prev, learning_rate, momentum_coef, verbose=False):
        '''
        Calculate the velocity
        '''

        args_argumented = list(args)
        for i in range(len(args_argumented)):
            args_argumented[i] += momentum_coef * velocity_prev[i]

        grad = self.fn_grad(*args_argumented)

        velocity = []
        for i in range(len(velocity_prev)):
            velocity.append(momentum_coef * velocity_prev[i] - learning_rate * grad[i])

        return velocity
    
    def find_min(self, args_init, n_max_iter, learning_rate, momentum_coef, tol, verbose=False):
        '''
        Find the args to minimize the loss function by using the given parameters
        '''

        args = list(args_init)
        loss = self.fn_loss(*args)
        grad = self.fn_grad(*args)

        args_lst = [tuple(args)]
        loss_lst = [loss]

        velocity = [0] * len(args)
        
        if verbose:
            print('--- init: args: {} loss: {} grad: {} ---'.format(args, loss, grad))
        
        # iterate only if the loss is greater then the given tolerance
        if abs(loss) > tol:
            for i in range(n_max_iter):

                velocity = self.calc_velocity(args, velocity, learning_rate, momentum_coef, verbose)

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
