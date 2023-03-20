import facebook

message = """
Happy Birthday to You
Happy Birthday to You
Happy Birthday Dear (name)
Happy Birthday to You.

From good friends and true,
From old friends and new,
May good luck go with you,
And happiness too.
"""

def GetPerString(message):
    for line in message.splitlines():
        for word in line.split():
            print(word)


GetPerString(message)
