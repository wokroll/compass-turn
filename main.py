def direction(facing, turn):
    directions = {
        "N": 0,
        "NE": 45,
        "E": 90,
        "SE": 135,
        "S": 180,
        "SW": 225,
        "W": 270,
        "NW": 315,
    }
    try:
        turn = int(turn)
    except ValueError:
        print("Enter a numeric value for turn between -1080 and 1080")
        return "Wrong turn"
    
    if facing not in directions.keys():
        print("Facing doesn`t belong to recognised direction.Please select one of these:")
        print(*directions.keys(), sep = ", ")
        return "Wrong facing"
        
    elif turn % 45 != 0 or turn > 1080 or turn < -1080:
        print("Turn not in proper range: between -1080 and 1080 degrees")
        return "Wrong turn"
        
    else:
        result_direction = (directions[facing]+turn) % 360
        for key, value in directions.items():
            if result_direction == value:
                result =  key
    
        return result
