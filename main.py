import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from cli.app import CLIApp

if __name__ == "__main__":
    app = CLIApp()
    app.run()