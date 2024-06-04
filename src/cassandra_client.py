from cassandra.cluster import Cluster

class CassandraClient:
    def __init__(self, nodes, keyspace):
        self.cluster = Cluster(nodes)
        self.session = self.cluster.connect(keyspace)

    # GetUserRole&Delete
    def get_user_role(self, username):
        query = "SELECT role FROM users WHERE username=%s ALLOW FILTERING"
        result = self.session.execute(query, (username,)).one()
        return result.role if result else None

    def delete_user(self, user_id):
        query = "DELETE FROM users WHERE user_id = %s"
        self.session.execute(query, (user_id,))


    # User
    def create_user(self, user_id, username, email, password, role):
        query = """
        INSERT INTO users (user_id, username, email, password, role)
        VALUES (%s, %s, %s, %s, %s)
        """
        self.session.execute(query, (user_id, username, email, password, role))

    def get_user(self, username):
        query = "SELECT * FROM users WHERE username=%s ALLOW FILTERING"
        return self.session.execute(query, (username,))
    
    # Role
    def create_role(self, role_name, permissions):
        query = """
        INSERT INTO roles (role_name, permissions)
        VALUES (%s, %s)
        """
        self.session.execute(query, (role_name, permissions))

    def get_role(self, role_name):
        query = "SELECT * FROM roles WHERE role_name=%s"
        return self.session.execute(query, (role_name,))