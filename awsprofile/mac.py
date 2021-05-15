import sys
import os
import re
from simple_term_menu import TerminalMenu
import rich
home_directory = os.path.expanduser("~")

def get_aws_profiles():
    aws_credential_file_path = os.path.join(home_directory, ".aws/credentials")
        
    aws_profiles = []
    aws_profile_name_regex = re.compile("^\[[A-z0-9]{1,}]$")
    
    lines = open(aws_credential_file_path, "r").read().splitlines()
    lines = [line.replace(" ", "") for line in lines if line]
    
    for line in lines:
        aws_profile_name_matched = aws_profile_name_regex.search(line)
        if aws_profile_name_matched:
            aws_profile_name = aws_profile_name_matched.group()[1:-1]
            aws_profiles.append(aws_profile_name)
    
    return aws_profiles

def main():
    args = sys.argv[1:]
    
    # read zshrc file
    zshrc_path = os.path.join(home_directory, ".zshrc")
    zshrc_read = open(zshrc_path, "r")
    zshrc_lines = zshrc_read.readlines()
    zshrc_read.close()
    
    if len(args) == 0:
        aws_profiles = get_aws_profiles()
        profile_name = aws_profiles[TerminalMenu(aws_profiles).show()]
        
        changed_profile = False
        
        for i in range(len(zshrc_lines)):
            line = zshrc_lines[i].replace(" ", "")
            if "exportAWS_PROFILE=" in line:
                zshrc_lines[i] = "export AWS_PROFILE=" + profile_name + "\n"
                changed_profile = True
                break
        
        if changed_profile == False:
            zshrc_lines.append("export AWS_PROFILE=" + profile_name + "\n")
        
        zshrc = open(zshrc_path, "w")
        zshrc.writelines(zshrc_lines)
        zshrc.close()
        
        rich.print("[bold green]SUCCESS: [white]Your AWS profile is changed [green]=> [white]" + profile_name, "[bold]")
        print()
        rich.print("[bold green]Open a new tab to load new AWS profile")
    elif args[0] == "now":
        for i in range(len(zshrc_lines)):
            line = zshrc_lines[i].replace(" ", "").replace("\n", "")
            if "exportAWS_PROFILE=" in line:
                aws_profile = line.split("=")[1]
                rich.print("[bold]Your default AWS profile [bold green]=> [white]" + aws_profile)
                
    else:
        rich.print("[bold red]ERROR: It occured an error when running the program")