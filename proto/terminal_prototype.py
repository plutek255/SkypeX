#!/usr/bin/env python3
"""
SkypeX Matrix Terminal Prototype
A bones-and-muscles terminal client for Matrix
"""

import asyncio
import sys
from getpass import getpass
from nio import AsyncClient, RoomMessageText, MatrixRoom, Event

class MatrixTerminalClient:
    """Simple terminal Matrix client"""

    def __init__(self, homeserver, username, password):
        self.homeserver = homeserver
        self.username = username
        self.password = password
        self.client = None
        self.rooms = {}
        self.sync_token = None

    async def connect(self):
        """Connect to Matrix homeserver"""
        print(f"Connecting to {self.homeserver}...")
        
        self.client = AsyncClient(self.homeserver, self.username)
        
        # Login
        print(f"Logging in as {self.username}...")
        response = await self.client.login(self.password)
        
        if response:
            print("✓ Login successful!")
            print(f"  Device ID: {self.client.device_id}")
            return True
        else:
            print("✗ Login failed")
            return False

    async def sync_rooms(self):
        """Sync and list rooms"""
        print("\nSyncing rooms...")
        
        response = await self.client.sync(timeout=10000)
        self.sync_token = response.next_batch
        
        # Collect rooms
        for room_id, room_info in response.rooms.join.items():
            self.rooms[room_id] = {
                'name': self._get_room_name(room_id, room_info),
                'unread': len(room_info.timeline.events)
            }
        
        for room_id, room_info in response.rooms.invite.items():
            self.rooms[room_id] = {
                'name': self._get_room_name(room_id, room_info),
                'unread': 'invite'
            }
        
        print(f"✓ Found {len(self.rooms)} rooms")
        return self.rooms

    def _get_room_name(self, room_id, room_info):
        """Get room name from room info"""
        # Try to get name from room state
        if hasattr(room_info, 'name') and room_info.name:
            return room_info.name
        
        # Fallback to room ID
        return room_id

    def list_rooms(self):
        """List all rooms"""
        print("\n" + "="*60)
        print("ROOMS")
        print("="*60)
        
        for i, (room_id, info) in enumerate(self.rooms.items(), 1):
            unread = info['unread']
            if unread == 'invite':
                status = "[INVITE]"
            elif unread > 0:
                status = f"[{unread} new]"
            else:
                status = "[read]"
            
            print(f"{i}. {status} {info['name']}")
            print(f"   ID: {room_id}")
            print()

    async def view_room(self, room_index):
        """View messages in a room"""
        room_ids = list(self.rooms.keys())
        
        if room_index < 1 or room_index > len(room_ids):
            print("Invalid room number")
            return
        
        room_id = room_ids[room_index - 1]
        room_name = self.rooms[room_id]['name']
        
        print(f"\n{'='*60}")
        print(f"ROOM: {room_name}")
        print(f"ID: {room_id}")
        print(f"{'='*60}\n")
        
        # Sync messages
        response = await self.client.sync(
            since=self.sync_token,
            timeout=10000,
            room_filter={
                'room': {
                    'timeline': {
                        'limit': 50
                    }
                }
            }
        )
        
        self.sync_token = response.next_batch
        
        # Display messages
        if room_id in response.rooms.join:
            events = response.rooms.join[room_id].timeline.events
            
            if not events:
                print("No recent messages")
            else:
                for event in reversed(events):
                    if isinstance(event, RoomMessageText):
                        sender = event.sender
                        body = event.body
                        timestamp = event.server_timestamp
                        
                        print(f"[{sender}]: {body}")
                        print()
        else:
            print("No messages available (room not joined)")

    async def send_message(self, room_index, message):
        """Send a message to a room"""
        room_ids = list(self.rooms.keys())
        
        if room_index < 1 or room_index > len(room_ids):
            print("Invalid room number")
            return
        
        room_id = room_ids[room_index - 1]
        
        print(f"Sending to {self.rooms[room_id]['name']}...")
        
        await self.client.room_send(
            room_id,
            message_type="m.room.message",
            content={
                "msgtype": "m.text",
                "body": message
            }
        )
        
        print("✓ Message sent")

    async def close(self):
        """Close connection"""
        if self.client:
            await self.client.close()
            print("\n✓ Disconnected")

def print_help():
    """Print help menu"""
    print("\n" + "="*60)
    print("COMMANDS")
    print("="*60)
    print("1. list    - List all rooms")
    print("2. view N  - View room N (use room number from list)")
    print("3. send N  - Send message to room N")
    print("4. sync    - Sync rooms")
    print("5. help    - Show this help")
    print("6. quit    - Exit")
    print("="*60)

async def main():
    """Main terminal interface"""
    print("="*60)
    print("SkypeX Matrix Terminal Prototype")
    print("="*60)
    
    # Get credentials
    homeserver = input("Matrix homeserver (e.g., https://matrix.org): ").strip()
    if not homeserver.startswith('http'):
        homeserver = f"https://{homeserver}"
    
    username = input("Matrix username (e.g., @user:matrix.org): ").strip()
    password = getpass("Password: ")
    
    # Connect
    client = MatrixTerminalClient(homeserver, username, password)
    
    if not await client.connect():
        print("Failed to connect. Exiting.")
        return
    
    # Initial sync
    await client.sync_rooms()
    client.list_rooms()
    
    print_help()
    
    # Main loop
    while True:
        try:
            command = input("\n> ").strip().lower()
            
            if not command:
                continue
            
            if command == 'quit' or command == 'exit' or command == 'q':
                break
            
            elif command == 'help' or command == 'h':
                print_help()
            
            elif command == 'list' or command == 'l':
                await client.sync_rooms()
                client.list_rooms()
            
            elif command == 'sync' or command == 's':
                print("Syncing...")
                await client.sync_rooms()
                print("✓ Sync complete")
            
            elif command.startswith('view '):
                try:
                    room_num = int(command.split()[1])
                    await client.view_room(room_num)
                except (ValueError, IndexError):
                    print("Usage: view N (where N is room number)")
            
            elif command.startswith('send '):
                parts = command.split(maxsplit=2)
                if len(parts) < 3:
                    print("Usage: send N message")
                    continue
                
                try:
                    room_num = int(parts[1])
                    message = parts[2]
                    await client.send_message(room_num, message)
                except ValueError:
                    print("Invalid room number")
            
            else:
                print(f"Unknown command: {command}")
                print("Type 'help' for available commands")
        
        except KeyboardInterrupt:
            print("\nInterrupted")
            break
        except Exception as e:
            print(f"Error: {e}")
    
    # Cleanup
    await client.close()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nExiting...")
