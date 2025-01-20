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
        print("Username: {}, UID: {}, GID: {}, Home Directory: {}, Shell: {}".format(
            user.pw_name, user.pw_uid, user.pw_gid, user.pw_dir, user.pw_shell))

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
        print("Group Name: {}, GID: {}, Members: {}".format(group.gr_name, group.gr_gid, members))

    # Print groups without members
    print_header("\nGroups without members:")
    for group in groups_without_members:
        print("Group Name: {}, GID: {}, Members: None".format(group.gr_name, group.gr_gid))

if __name__ == "__main__":
    enumerate_users()
    enumerate_groups()
