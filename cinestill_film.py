def calculate_film_development_time():
    try:
        uses = int(input("Enter the number of times you've used the liquid (1-24): "))
        if uses < 1:
            print("Please enter an integer greater than 0.")
            return
        elif uses > 24:
            print("The maximum for chemical is 24, you should consider using new chemical.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer between 1 and 24.")
        return

    # Initial times in seconds
    developing_time_s = 210  # 3 minutes 30 seconds
    fixing_time_s = 480      # 8 minutes
    
    # Increase times by 4% for each additional use
    for _ in range(1, uses):
        developing_time_s *= 1.04
        fixing_time_s *= 1.04
        
    # Convert seconds to minutes:seconds format
    developing_time_min = int(developing_time_s // 60)
    developing_time_sec = developing_time_s % 60
    fixing_time_min = int(fixing_time_s // 60)
    fixing_time_sec = fixing_time_s % 60
    
    # Output results in seconds and minutes:seconds format
    print(f"Developing time: {developing_time_s:.2f} seconds ({developing_time_min}mins {developing_time_sec:.1f}s)")
    print(f"Fixing time: {fixing_time_s:.2f} seconds ({fixing_time_min}mins {fixing_time_sec:.1f}s)")

    # Additional warnings based on the number of uses
    if uses > 12:
        print("Warning: The provided times are based on 1000ml of chemical. If your volume is 500ml, the chemical may not be effective for the film.")

#Let user input the number of times they've used the liquid
#uses = int(input("Enter the number of times you've used the liquid: "))
calculate_film_development_time()

if __name__ == "__main__":
    pass
