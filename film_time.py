def calculate_film_development_time(uses):
    # Initial times in seconds
    developing_time_s = 210  # 3 minutes 30 seconds
    fixing_time_s = 480      # 8 minutes
    
    # Increase times by 4% for each additional use
    for _ in range(1, uses):
        developing_time_s *= 1.04
        fixing_time_s *= 1.04
        
    # Convert seconds to minutes:seconds format
    developing_time_min = int(developing_time_s // 60)
    developing_time_sec = round(developing_time_s % 60, 2)
    fixing_time_min = int(fixing_time_s // 60)
    fixing_time_sec = round(fixing_time_s % 60, 2)
    
    # Define result dictionary here
    result = {
       'developing_time_formatted': f"{developing_time_min}mins {developing_time_sec}s",
        'fixing_time_formatted': f"{fixing_time_min}mins {fixing_time_sec}s",
        'developing_time_seconds': f"{round(developing_time_s, 2)}s",  # Total time in seconds, rounded
        'fixing_time_seconds': f"{round(fixing_time_s, 2)}s",  # Total time in seconds, rounded
    }

    # Add any conditional warnings
    if uses > 12:
        result['warning'] = "Warning: The provided times are based on 1000ml of chemical. If your volume is 500ml, the chemical may not be effective for the film."
    
    return result
