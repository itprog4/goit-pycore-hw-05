from task1 import caching_fibonacci
from task3 import sum_profit, generator_numbers

if __name__ == '__main__':
    # task 1
    fib = caching_fibonacci()

    print(fib(10))
    print(fib(15))

    # rask 2
    text1 = 'The total profit for the quarter was 123.45 USD, and the average profit per day was 45.67 USD.'
    text2 = 'Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.'
    print(sum_profit(text1, generator_numbers))
    print(sum_profit(text2, generator_numbers))