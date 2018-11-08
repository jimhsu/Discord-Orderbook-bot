PREFIX = "!"
HELPER = "Correct format: !wtb Nyzo Sats\nEx. !wtb 1000 500"
INVALIDMARKET = "No such market found.\nCorrect format: !market"
INVALIDHELP = "Try using '!help' instead."
INVALIDCLEAR = "Try using '!clear' instead."
MAXORDERS = 2
INMAX= "Maximum amount of orders per user: " + str(MAXORDERS)
CURRENCY = "nyzo"
CURRENCY2 = "sats"
HELP = "**Welcome to NyzoBot!**\n\nCommands:\n!wtb {} {}\n!wts {} {}\n!market\n!clear\n\nFor buy and sell orders, fill in the {} price **per** {}.".format(CURRENCY, CURRENCY2, CURRENCY, CURRENCY2, CURRENCY2, CURRENCY)