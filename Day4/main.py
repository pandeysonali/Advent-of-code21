def isWinner(board):
	#Check rows
	start = 0
	for i in range(5):
		if board[start] + board[start+1] + board[start+2] + board[start+3] + board[start+4] == 500:
			return True
		start += 5
	#Check cols
	start = 0
	for i in range(5):
		if board[start] + board[start+5] + board[start+10] + board[start+15] + board[start+20] == 500:
			return True
		start += 1

	return False


