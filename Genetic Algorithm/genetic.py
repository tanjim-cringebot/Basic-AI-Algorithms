import random

# Define function to parse input transactions
def parse_input(n, transactions):
    types = []
    amounts = []
    for i in range(n):
        t, amount = transactions[i].split()
        if t == 'd':
            types.append(1)
        else:
            types.append(-1)
        amounts.append(int(amount))
    return types, amounts

# Define fitness function
def fitness(register, types, amounts):
    total = 0
    for i in range(len(register)):
        if register[i] == 1:
            sum = 0
            for j in range(len(register)):
                if register[j] == 1:
                    sum += types[j] * amounts[j]
            if sum == 0:
                total += abs(amounts[i])
    return total

# Define crossover function
def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

# Define mutation function
def mutation(register, probability):
    for i in range(len(register)):
        if random.random() < probability:
            register[i] = 1 - register[i]
    return register

# Define function to generate a random register
def generate_random_register(length):
    register = []
    for i in range(length):
        register.append(random.randint(0, 1))
    return register

# Define main function
def main():
    # Get number of transactions
    n = int(input())

    # Get list of transactions
    transactions = []
    for i in range(n):
        transactions.append(input())

    # Parse transactions into types and amounts
    types, amounts = parse_input(n, transactions)

    # Set population size and register length
    population_size = 1000
    register_length = n

    # Generate initial population of random registers
    population = []
    for i in range(population_size):
        population.append(generate_random_register(register_length))

    # Set maximum number of iterations and mutation probability
    max_iterations = 1000
    mutation_probability = 0.01

    # Iterate until a valid register is found or the maximum number of iterations is reached
    for i in range(max_iterations):
        # Calculate fitness of each register in population
        fitnesses = []
        for register in population:
            fitnesses.append(fitness(register, types, amounts))

        # If a register with non-zero fitness is found, print it and return
        if any(fitnesses):
            best_register = population[fitnesses.index(max(fitnesses))]
            print(''.join(map(str, best_register)))
            return

        # If all registers have zero fitness, print -1 and return
        non_zero_fitnesses = []
        for f in fitnesses:
            if f != 0:
                non_zero_fitnesses.append(f)
        if not non_zero_fitnesses:
            print('-1')
            return

        # Select two parents based on fitness and generate a child through crossover and mutation
        parent1, parent2 = random.choices(population, weights=fitnesses, k=2)
        child = crossover(parent1, parent2)
        child = mutation(child, mutation_probability)

        # Replace a random member of the population with the new child
        population[random.randint(0, population_size - 1)] = child

    # If maximum number of iterations is reached without finding a valid register, print -1
    print('-1')

# Call main function
if __name__ == '__main__':
    main()
