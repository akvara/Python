import sys
if __name__ == "__main__":
    # execute only if run as a script
    arg_names = ['command', 'input', 'output']
    args = dict(zip(arg_names, sys.argv))
    if not 'input' in args:
        print "Usage: " + args["command"] + " input [output]"
        exit(-1)
    input_file = args["input"]
    try:
        file = open(input_file,"r")
        str = file.read()
        file.close()
        print('"' + '" "'.join(str.split()) + '"')
    except:
        print "File " + input_file + " does not exist"
        exit(-1)
 