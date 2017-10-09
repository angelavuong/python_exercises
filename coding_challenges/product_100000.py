from datetime import datetime

def calcProd():
    # Calculate the product of the first 100,000 numbers
    product = 1
    for i in range(1,100000):
        product = product * i
    return product

start_time = datetime.now()
answer = calcProd()
print ("The product of the first 100,000 numbers is " + str(answer))
end_time = datetime.now()
execution_time = end_time - start_time
print ("It took " + str(execution_time) + " to complete this calculation.")
