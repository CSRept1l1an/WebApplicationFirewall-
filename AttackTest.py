from SQLi import detect_sql_injection, cur, connection
from XSS import detect_xss
import socket

def attack_tester(user_input):
    ip_address = socket.gethostbyname(socket.gethostname())

    if detect_sql_injection(user_input):
        attack_type = "SQL Injection"
    elif detect_xss(user_input):
        attack_type = "XSS Attack"

    def log_attack(ip_address, attack_type):
        cur.execute("INSERT INTO attacks (attack_type, ip_address) VALUES (?, ?)", (attack_type, ip_address))
        connection.commit()
        print(f"Attack detected: {attack_type} from IP {ip_address}")

        log_attack(ip_address, attack_type)
