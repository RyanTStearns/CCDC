import pwd
import grp
from termcolor import colored

# Function to print headers in color
def print_header(text):
    print(colored(text, 'yellow', attrs=['bold']))

# Function to print user details in a clean format
def enumerate_users():
    """Enumerates all users on the Linux system."""
    print_header("\n--- Users ---")
    for user in pwd.getpwall():
        print(f"Username: {colored(user.pw_name, 'cyan')}, UID: {colored(user.pw_uid, 'green')}, "
              f"GID: {colored(user.pw_gid, 'green')}, Home Directory: {colored(user.pw_dir, 'blue')}, "
              f"Shell: {colored(user.pw_shell, 'blue')}")

# Function to print groups with and without members
def enumerate_groups():
    """Enumerates all groups on the Linux system."""
    print_header("\n--- Groups ---")
    groups_with_members = []
    groups_without_members = []

    # Separate groups with and without members
    for group in grp.getgrall():
        if group.gr_mem:
            groups_with_members.append(group)
        else:
            groups_without_members.append(group)

    # Print groups with members
    print_header("\nGroups with members:")
    for group in groups_with_members:
        members = ", ".join(group.gr_mem)
        print(f"Group Name: {colored(group.gr_name, 'cyan')}, GID: {colored(group.gr_gid, 'green')}, "
              f"Members: {colored(members, 'magenta')}")

    # Print groups without members
    print_header("\nGroups without members:")
    for group in groups_without_members:
        print(f"Group Name: {colored(group.gr_name, 'cyan')}, GID: {colored(group.gr_gid, 'green')}, "
              f"Members: {colored('None', 'red')}")

if __name__ == "__main__":
    enumerate_users()
    enumerate_groups()
