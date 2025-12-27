import sys

def print_bear(message):
    print(f"""
   __         __
  /  \\.-"'-./  \\
  \\    -   -    /
   |   o   o   |
   \\  .-'''-.  /
    '-\\__Y__/-'
       `---`
      /
  ( {message} )
    """)

if __name__ == "__main__":
    msg = "Hello, World!"
    if len(sys.argv) > 1:
        msg = " ".join(sys.argv[1:])
    print_bear(msg)
