def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    if from_member not in social_graph[to_member]["following"] and to_member not in social_graph[from_member]["following"]:
        str = "no relationship"
    elif from_member in social_graph[to_member]["following"] and to_member in social_graph[from_member]["following"]:
        str = "friends"
    elif from_member in social_graph[to_member]["following"]:
        str = "followed by"
    elif to_member in social_graph[from_member]["following"]:
        str = "follower"
        
    return str
    

def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    if len(board) == 3:
        #column and rows
        for column in range(0,3):
            if board[0][column] == board[1][column] == board[2][column] != '':
                str = board[0][column]
                return str
        
        for row in range(0,3):
            if board[row][0] == board[row][1] == board[row][2] != '':
                str = board[row][0]
                return str
        
        #diagonals
        if board[0][0] == board[1][1] == board[2][2] != '':
            str = board[0][0]
            return str
        elif board[0][2] == board[1][1] == board[2][0] != '':
            str = board[0][2]
            return str
        
    if len(board) == 4:
        #column and rows
        for column in range(0,4):
            if board[0][column] == board[1][column] == board[2][column] == board[3][column] != '':
                str = board[0][column]
                return str
        for row in range(0,4):
            if board[row][0] == board[row][1] == board[row][2] == board[row][3] != '':
                str = board[row][0]
                return str
        
        #diagonals
        if board[0][0] == board[1][1] == board[2][2] == board[3][3] != '':
            str = board[0][0]
            return str
        elif board[0][3] == board[1][2] == board[2][1] == board[3][0] != '':
            str = board[0][3]
            return str
        
    if len(board) == 5:
        #column and rows
        for column in range(0,5):
            if board[0][column] == board[1][column] == board[2][column] == board[3][column] == board[4][column] != '':
                str = board[0][column]
                return str
        for row in range(0,5):
            if board[row][0] == board[row][1] == board[row][2] == board[row][3] == board[row][4] != '':
                str = board[row][0]
                return str
        
        #diagonals
        if board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4] != '':
            str = board[0][0]
            return str
        elif board[0][4] == board[1][3] == board[2][2] == board[3][1] == board[4][0] != '':
            str = board[0][4]
            return str
    
    if len(board) == 6:
        #column and rows
        for column in range(0,6):
            if board[0][column] == board[1][column] == board[2][column] == board[3][column] == board[4][column] == board[5][column] != '':
                str = board[0][column]
                return str
        for row in range(0,6):
            if board[row][0] == board[row][1] == board[row][2] == board[row][3] == board[row][4] == board[row][5] != '':
                str = board[row][0]
                return str
        
        #diagonals
        if board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4] == board[5][5] != '':
            str = board[0][0]
            return str
        elif board[0][5] == board[1][4] == board[2][3] == board[3][2] == board[4][1] == board[5][0] != '':
            str = board[0][5]
            return str
    
    str = "NO WINNER"
    return str

def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
     
    legs = tuple(route_map.keys())  
    total_time = 0  
    next_stop = None  
    while first_stop != second_stop:  
        if (first_stop, second_stop) in route_map:
            total_time += route_map[(first_stop, second_stop)]['travel_time_mins']
            break  
        else:
            for leg in route_map:
                if leg[0] == first_stop:
                    next_stop = leg[1]  
                    total_time += route_map[leg]['travel_time_mins']  
                    break
            if next_stop is None:
                break
            first_stop = next_stop  
    return total_time