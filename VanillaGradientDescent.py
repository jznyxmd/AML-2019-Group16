class VanillaGradientDescent:
    ''' Generalized Vanilla Gradient Descent Class '''

    def __init__(self, fn_loss, fn_grad):
        self.fn_loss = fn_loss
        self.fn_grad = fn_grad

    def find_min(self, args_init, n_max_iter, learning_rate, tol, verbose=False):
        '''
        Find the args to minimize the loss function by using the given parameters
        '''

        args = list(args_init)
        loss = self.fn_loss(*args)
        grad = self.fn_grad(*args)

        args_lst = [tuple(args)]
        loss_lst = [loss]
        
        if verbose:
            print('--- init: args: {} loss: {} grad: {} ---'.format(args, loss, grad))
        
        # iterate only if the loss is greater then the given tolerance
        if abs(loss) > tol:
            for i in range(n_max_iter):

                for j in range(len(args)):
                    args[j] -= learning_rate * grad[j]

                loss = self.fn_loss(*args)

                args_lst.append(tuple(args))
                loss_lst.append(loss)

                if abs(loss) <= tol:
                    break

                grad = self.fn_grad(*args)

                if verbose:
                    print('iter: {} args: {} loss: {} grad: {}'.format(i, args, loss, grad))
        
        if verbose:
            print('--- final: args: {} loss: {} grad: {} ---'.format(args, loss, grad))

        return (args, args_lst, loss_lst)
