"""Simple if/else chatbot.

This script provides a small command-line chatbot implemented with
straightforward if/elif/else branching. It's intentionally simple so it's
easy to read and extend.

Usage:
    python chatbot.py

Type 'quit' or 'exit' to stop the bot.
"""

import random
import sys


def respond(message: str) -> str:
    """Return a chatbot reply using simple if/else rules.

    The function lower-cases and strips the input and then matches it
    against a few categories. If no rule matches, a fallback answer is
    returned.
    """
    msg = message.strip().lower()

    # greetings
    if msg in ('hi', 'hello', 'hey', 'good morning', 'good afternoon'):
        return random.choice(['Hello!', 'Hi there!', "Hey — what's up?"])

    # ask name
    if 'your name' in msg or msg.startswith('who are you'):
        return "I'm a simple chatbot that uses if/else rules. You can call me Bot." 

    # farewell
    if msg in ('bye', 'goodbye', 'see you', 'quit', 'exit'):
        return 'Goodbye! Have a nice day.'

    # time / date
    if 'time' in msg:
        from datetime import datetime
        return 'Current time is ' + datetime.now().strftime('%H:%M:%S')

    if 'date' in msg or 'day' in msg:
        from datetime import datetime
        return 'Today is ' + datetime.now().strftime('%Y-%m-%d')

    # simple math (very small support)
    if msg.startswith('add ') or msg.startswith('sum '):
        # expected format: 'add 2 and 3' or 'add 2 3'
        nums = [int(s) for s in msg.replace('and', ' ').split() if s.lstrip('-').isdigit()]
        if len(nums) >= 2:
            return f'The sum is {sum(nums)}'
        return 'I could not find two numbers to add.'

    # how are you
    if 'how are you' in msg or 'how r you' in msg:
        return random.choice(["I'm fine, thanks!", "Doing well — thanks for asking."])

    # fallback responses
    fallbacks = [
        "Sorry, I don't understand. Can you rephrase?",
        "Hmm — I'm not sure about that.",
        "I can answer basic questions about time, date, math (add), or say hi."
    ]
    return random.choice(fallbacks)


def repl():
    """Read-eval-print loop for interactive chat in the terminal."""
    print('Simple Bot — type a message (type "quit" or "exit" to stop)')
    try:
        while True:
            msg = input('You: ').strip()
            if not msg:
                continue
            # if user asked to quit, print goodbye and break
            if msg.lower() in ('quit', 'exit'):
                print('Bot: Goodbye!')
                break
            reply = respond(msg)
            print('Bot:', reply)
    except (KeyboardInterrupt, EOFError):
        print('\nBot: Goodbye!')


if __name__ == '__main__':
    # If arguments are provided, treat them as a single message and print
    # the bot's response then exit. Otherwise enter REPL.
    if len(sys.argv) > 1:
        message = ' '.join(sys.argv[1:])
        print(respond(message))
    else:
        repl()
