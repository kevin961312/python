 import scipy.optimize as opt
    from numpy import exp
    import timeit

    st1 = timeit.default_timer()

    def f(variables) :
        (x,y) = variables

        first_eq = x + y**2 -4
        second_eq = exp(x) + x*y - 3
        return [first_eq, second_eq]

    solution = opt.fsolve(f, (0.1,1) )
    print(solution)


    st2 = timeit.default_timer()
    print("RUN TIME : {0}".format(st2-st1))

->

[ 0.62034452  1.83838393]
RUN TIME : 0.0009331008900937708
