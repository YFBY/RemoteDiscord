import subprocess
import time
import json
import socket

with open("config.json") as cf:
    ConfigFile = json.load(cf)

class server:
    ServerType = None
    ServerProcess = None
    ServerOutput = None

    def __init__(self, ServerOutput="Server.log"):
        self.ServerOutput = ServerOutput

    def input(self, ServerInput): # fix this
        if self.ServerProcess.poll() is None:
            #self.ServerProcess.communicate(input=ServerInput)
            self.ServerProcess.stdin.write(ServerInput)
        else:
            return "No Server Running."

    def output(self): #Return Server Output
        if self.ServerProcess.poll() is None:
            with open(self.ServerOutput, 'r') as file_output:
                try:
                    return file_output.read()[-1499:]
                
                except IndexError:
                    return file_output.read()
        else:
            return "No Server Running."

    def state(self): #Return State Of Server
        if self.ServerProcess:
            return [self.ServerProcess.poll(), self.ServerType]
        else:
            return False
    
    def start(self, SelectedServer): #Start A Server
        try:
            if self.ServerProcess.poll() is None:
                return f"Server or command is already Running {self.ServerType}."

        except AttributeError:
            pass
        
        if ConfigFile["Servers"].get(SelectedServer):
            self.ServerType = SelectedServer
            with open(self.ServerOutput, 'w') as output:
                self.ServerProcess = subprocess.Popen(ConfigFile["Servers"].get(SelectedServer), shell=True, text=True, stdin=subprocess.PIPE, stderr=output, stdout=output)
                return f"Running \"{SelectedServer}\" Server."
        else:
            return f"{SelectedServer} Was Not Found."




    #make this REAL
    def run(self, SelectedServer): #Start A Server
        try:
            if self.ServerProcess.poll() is None:
                return f"Server is already Running {self.ServerType}."

        except AttributeError:
            pass
        
        if ConfigFile["Servers"].get(SelectedServer):
            self.ServerType = SelectedServer
            with open(self.ServerOutput, 'w') as output:
                self.ServerProcess = subprocess.Popen(ConfigFile["Servers"].get(SelectedServer), shell=True, text=True, stdin=subprocess.PIPE, stderr=output, stdout=output)
                return f"Running \"{SelectedServer}\" Server."
        else:
            return f"{SelectedServer} Was Not Found."

    #add function to kill process


    @staticmethod
    def ip(): #get the ip
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            LocalIP = s.getsockname()[0]
            s.close()
            return LocalIP
        except Exception as error:
            print(error)
