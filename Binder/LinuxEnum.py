import pwd
import grp

# Function to print headers
def print_header(text):
    print(text)

# Function to print user details in a clean format
def enumerate_users():
    """Enumerates all users on the Linux system."""
    print_header("\n--- Users ---")
    for user in pwd.getpwall():
        print(f"Username: {user.pw_name}, UID: {user.pw_uid}, "
              f"GID: {user.pw_gid}, Home Directory: {user.pw_dir}, "
              f"Shell: {user.pw_shell}")

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
        print(f"Group Name: {group.gr_name}, GID: {group.gr_gid}, Members: {members}")

    # Print groups without members
    print_header("\nGroups without members:")
    for group in groups_without_members:
        print(f"Group Name: {group.gr_name}, GID: {group.gr_gid}, Members: None")

if __name__ == "__main__":
    enumerate_users()
    enumerate_groups()
