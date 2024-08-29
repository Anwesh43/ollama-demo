import ollama 
import sys 
def generateCode(input : str): 
    return ollama.generate(model = 'codellama', prompt = input)

def writeCode(fileName : str, output):
    with open(fileName, 'w') as f:
        f.write(output)

def main():
    if len(sys.argv) == 3:
        print("Generating code")
        output = generateCode(sys.argv[1])
        print("Writing code to file", output)
        writeCode(sys.argv[2], output['response'])

if __name__ == "__main__":
    main()
