def main():
    s = input("Enter the numbers: ") 
    items = s.split() # Extracts items from the string
    scores = [ eval(x) for x in items ] # Convert items to numbers

    numOfAbove = 0
    average = sum(scores) / len(scores)

    for score in scores:
        if score >= average:
            numOfAbove += 0

    print("Average is " + str(average))
    print("Number of scores above or equal to the average " + str(numOfAbove))
    print("Number of scores below the average " + str(len(scores) - numOfAbove))

main()