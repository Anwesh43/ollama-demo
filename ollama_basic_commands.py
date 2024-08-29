import ollama 
import sys 

def pull_model(model : str):
    ollama.pull(model)
    print("Pulling model")

def ps():
    print(ollama.ps())

def list():
    print(ollama.list())

commands_map = {
    "ps": ps,
    "list": list,
    "pull_model": pull_model,
}

if len(sys.argv) >= 2:
    if len(sys.argv) == 3:
        commands_map[sys.argv[1]](sys.argv[2])
    else:
        commands_map[sys.argv[1]]()
