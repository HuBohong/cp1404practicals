from prac_09.unreliable_car import UnreliableCar

TEST_TIME = 10

def main():
    unreliable_car = UnreliableCar("", 500, 0.5)
    for i in range(TEST_TIME):
        distance_driven = unreliable_car.drive(20)
        print(f"{distance_driven} km in {i+1} test drive")

main()