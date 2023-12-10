import time

class Packet:
    def __init__(self, content):
        self.content = content
        
class Alice:
    def __init__(self):
        self.outgoing_packets = []
        
    def create_packet(self, content):
        packet = Packet(content)
        self.outgoing_packets.append(packet)
        
    def has_packets_to_send(self):
        return len(self.outgoing_packets) > 0
    
    def send_packets_to_bob(self, bob):
        if self.has_packets_to_send():
            packet = self.outgoing_packets.pop(0)
            bob.receive_packet(packet)
            print(f"Alice sends: {packet.content}")
            return packet
        
class Bob:
    def __init__(self):
        self.incoming_packets = []
        
    def has_packets_from_alice(self):
        return len(self.incoming_packets) > 0
    
    def receive_packet(self, packet):
        self.incoming_packets.append(packet)
        
    def read_packet(self):
        if self.has_packets_from_alice():
            packet = self.incoming_packets.pop(0)
            print(f"Bob receives and reads: {packet.content}")
            
# Create Alice and Bob
alice = Alice()
bob = Bob()

for i in range(5):
    # Alice creates and sends packets
    alice.create_packet(f"Packet {i + 1}")
    alice.send_packets_to_bob(bob)
    
    # Bob checks for and reads packets
    if bob.has_packets_from_alice():
        bob.read_packet()
        
    # Add a delay to simulate the process
    time.sleep(1)