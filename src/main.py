import uuid
from cassandra_client import CassandraClient

def main():
    # Ersetze die IP-Adresse durch die tatsächliche IP-Adresse des Cassandra-Containers
    client = CassandraClient(['127.0.0.1'], 'user_management')

    # Erstelle einige Rollen
    client.create_role('Admin', {'create_user', 'update_user', 'delete_user', 'view_user'})
    client.create_role('Editor', {'create_user', 'update_user', 'view_user'})
    client.create_role('Viewer', {'view_user'})

    # Erstelle einige Benutzer
    client.create_user(uuid.uuid4(), 'john_doe', 'john@example.com', 'password123', 'Admin')
    client.create_user(uuid.uuid4(), 'jane_smith', 'jane@example.com', 'password456', 'Editor')

    # Abfrage der Benutzer
    users = client.get_user('john_doe')
    for user in users:
        print(user)

    # Abfrage der Rollen
    roles = client.get_role('Admin')
    for role in roles:
        print(role)

if __name__ == "__main__":
    main()