import random
import time
import numpy as np

class Chromosome:
    def __init__(self, genes, fitness):
        self.genes = genes
        self.fitness = fitness

def get_fitness(original, guess):
    counter = 0
    for i, j in zip(original, guess):
        if i == j:
            counter += 1
    return counter

def mutate(guess, dictionary, original):
    child = list(guess.genes)
    index = np.random.randint(0, len(guess.genes))
    new1, new2 = random.sample(dictionary, 2)

    if child[index] == new1:
        child[index] = new2
    else:
        child[index] = new1

    child_genes = ''.join(child)
    child_fitness = get_fitness(original, child_genes)

    return Chromosome(child_genes, child_fitness)

def generate_parent(original, guess):
    genes = []

    while len(genes) < len(original):
        size = min(len(original) - len(genes), len(guess))
        items = random.sample(guess, size)
        genes.extend(items)

    genes_class = ''.join(genes)
    genes_fitness = get_fitness(original, genes_class)

    return Chromosome(genes_class, genes_fitness)

def log(guess, iterations):
    print("{}\t{} \iteration {}".format(guess.genes, guess.fitness, iterations) )


original = "Hello there, it's me!"
guess = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.,'"

def launch(VERBOSE):
    best_parent = generate_parent(original, guess)
    Found = False
    iterations = 0

    while not Found:
        child = mutate(best_parent, guess, original)

        if child.fitness > best_parent.fitness:
            best_parent = child
            if VERBOSE:
                log(best_parent, iterations)

        if best_parent.fitness == len(original):
            Found = True

        iterations += 1

    if VERBOSE:
        print("{} {}, \t total iterations {}".format(best_parent.genes, best_parent.fitness, iterations) )
    return iterations

VERBOSE = False
def main(iterations = 200):
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
