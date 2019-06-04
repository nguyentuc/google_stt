import subprocess

def play():
    subprocess.Popen(['mpg123', '-q', 'resources/answer.mp3']).wait()