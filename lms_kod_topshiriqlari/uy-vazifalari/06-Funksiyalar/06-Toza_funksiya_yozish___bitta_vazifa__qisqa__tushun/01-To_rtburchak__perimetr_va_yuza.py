def perimetr(eni, boyi):
    return 2 * (eni + boyi)

def yuza(eni, boyi):
    return eni * boyi

if __name__ == '__main__':
    
    eni, boyi = map(int, input().split())
    
    print(perimetr(eni, boyi))
    print(yuza(eni, boyi))