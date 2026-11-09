import random


def load_songs(filename):
    """Load songs from the text file."""
    try:
        with open(filename, "r") as file:
            songs = [line.strip() for line in file if line.strip()]
        return songs

    except FileNotFoundError:
        print("Error: songs.txt file not found.")
        return []


def view_songs(songs):
    """Display all available songs."""
    print("\n=== Available Songs ===")

    for index, song in enumerate(songs, start=1):
        print(f"{index}. {song}")


def play_song(song, played_songs):
    """Play a selected song and track it."""
    if song in played_songs:
        print("This song has already been played.")
        return

    print(f"\nNow Playing: {song}")
    played_songs.append(song)


def play_random_song(songs, played_songs):
    """Play a random song without repetition."""
    remaining_songs = [
        song for song in songs if song not in played_songs
    ]

    if not remaining_songs:
        print("All songs have been played!")
        return

    song = random.choice(remaining_songs)
    play_song(song, played_songs)


def select_song(songs, played_songs):
    """Allow the user to select a song."""
    view_songs(songs)

    try:
        choice = int(input("\nEnter song number: "))

        if 1 <= choice <= len(songs):
            play_song(songs[choice - 1], played_songs)
        else:
            print("Invalid song number.")

    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    print("=== Music Streaming Assistant ===")

    songs = load_songs("songs.txt")
    played_songs = []

    if not songs:
        print("No songs available.")
        exit()

    while True:
        print("\nAvailable Commands:")
        print("1. Play a random song")
        print("2. View all songs")
        print("3. Select a song")
        print("4. Quit")

        command = input("\nEnter your command: ").strip().lower()

        if command in ["1", "play a random song"]:
            play_random_song(songs, played_songs)

        elif command in ["2", "view all songs"]:
            view_songs(songs)

        elif command in ["3", "select a song"]:
            select_song(songs, played_songs)

        elif command in ["4", "quit", "exit"]:
            print("Thank you for using Music Streamer!")
            break

        else:
            print("Invalid command. Please try again.")
