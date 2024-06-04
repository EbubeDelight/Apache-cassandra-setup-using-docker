import uuid
from cassandra_client import CassandraClient

def main():
    client = CassandraClient(['127.0.0.1'], 'user_management')

    # Role creation
    #client.create_role('Admin', {'create_user', 'update_user', 'delete_user', 'view_user'})
    #client.create_role('Editor', {'create_user', 'update_user', 'view_user'})
    #client.create_role('Viewer', {'view_user'})

    # User creation
    #client.create_user(uuid.uuid4(), 'john_doe', 'john@example.com', 'password123', 'Admin')
    #client.create_user(uuid.uuid4(), 'jane_smith', 'jane@example.com', 'password456', 'Editor')
    client.create_user(uuid.uuid4(), 'alice_smith', 'alice@example.com', 'password789', 'Viewer')
    client.create_user(uuid.uuid4(), 'bob_jones', 'bob@example.com', 'password012', 'Editor')

    # User query
    users = client.get_user('bob_jones')
    for user in users:
        print(user)

    # Query roles
    roles = client.get_role('Admin')
    for role in roles:
        print(role)

    # Admin check
    user_role = client.get_user_role('jane_smith')
    if user_role == 'Admin':
        client.delete_user(uuid.UUID('e09a08a8-4771-4a8f-85a1-4dd17120f763'))
        print("User 'jane_smith' deleted by 'john_doe'.")
    else:
        print("'john_doe' is not an admin and cannot delete users.")

if __name__ == "__main__":
    main()