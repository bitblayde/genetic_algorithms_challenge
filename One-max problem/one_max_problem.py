import random
import numpy as np
import time

class Chromosome:
    def __init__(self, genes, fitness):
        self.genes = genes
        self.fitness = fitness

def mutate( parent, dictionary ):
    child_genes = parent.genes[:]
    index = random.randint(0, len( parent.genes )-1 )
    new1, new2 = random.sample( dictionary, 2 )

    if child_genes[index] == new1:
        child_genes[index] = new2
    else:
        child_genes[index] = new1

    return Chromosome( child_genes, get_fitness( child_genes ) )

def get_parent( target_size ):
    genes = list(np.random.choice([0, 1], size = (target_size)))
    fitness = get_fitness(genes)

    return Chromosome(genes, fitness)

def get_fitness( genes ):
    return genes.count(1)

def launch(VERBOSE):
    initial_genes = [0, 1]
    target_size = 500
    iterations = 0

    best = get_parent( target_size )
    found = False


    while not found:
        child = mutate( best, initial_genes )

        if child.fitness >= best.fitness:
             best = child

             if VERBOSE:
                 print(best.fitness)
                 print(best.genes)

        if best.fitness >= target_size:
            found = True

        iterations+=1
    return iterations


def main(iterations = 200):
    VERBOSE = False
    mean = []
    it = 0

    for i in range(iterations):
        start = time.perf_counter()
        it += launch(VERBOSE)
        stop = time.perf_counter()
        mean.append( stop - start )

    print("time {:.6f}s, \t std {} \t mean iterations {}".format( np.mean(mean), np.std(mean), (it/iterations) ) )

if __name__ == "__main__":
    main()
