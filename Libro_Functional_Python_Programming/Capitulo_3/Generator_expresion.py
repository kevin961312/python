import math
import itertools
def pfactors1(numb):
    if numb % 2 ==0:
        yield 2
        if numb // 2 > 1:
            yield from pfactors1(numb//2)
        return 
    for itera in range(3, int(math.sqrt(numb)+0.5)+1,2):
        if numb % itera == 0:
            yield itera
            if numb // itera > 1:
                yield from pfactors1(numb//itera)
            return
    yield numb

generator = [ num for num in pfactors1(2)]
print(generator)
print(next(pfactors1(97496)))

def pfactorsr(numb):
    def factor_n(numb,itera):
        if itera > int(math.sqrt(numb)+0.5)+1:
            yield numb
            return
        if numb % itera ==0:
            yield itera
            if numb // itera > 1:
                yield from factor_n(numb//itera, itera)
        else:
            yield from factor_n(numb, itera+2)
    if numb % 2 == 0:
        yield 2
        if numb // 2 > 1:
            yield from pfactorsr(numb//2)
        return
    yield from factor_n(numb, 3)
    
generator1 = [ num for num in pfactorsr(256)]
print(generator1)
print(next(pfactorsr(97496)))

print(pfactors1(1560))
print(list(pfactors1(1560)))
#print(len(pfactors1(1560)))
result = pfactors1(1560)
print(sum(result))
#Los generadores solo se agrupan una vez, despues de ser llamados o usados se vacian.
print(sum(result))


def limits(iterable):
    max_tee, min_tee = itertools.tee(iterable,2)
    return max(max_tee), min(min_tee)

print(limits(pfactorsr(25985223)))