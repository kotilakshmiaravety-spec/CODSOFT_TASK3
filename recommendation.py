import random

movies = {
    "Action": [
        "Avengers",
        "John Wick",
        "Mission Impossible",
        "Mad Max"
    ],
    "Comedy": [
        "3 Idiots",
        "Jumanji",
        "The Mask",
        "Home Alone"
    ],
    "Horror": [
        "The Conjuring",
        "Annabelle",
        "Insidious",
        "The Nun"
    ],
    "Romance": [
        "Titanic",
        "The Notebook",
        "La La Land",
        "Me Before You"
    ],
    "Sci-Fi": [
        "Interstellar",
        "Inception",
        "Avatar",
        "The Matrix"
    ]
}

print("=" * 45)
print("      Movie Recommendation System")
print("=" * 45)

while True:
    print("\nAvailable Genres:")
    for genre in movies:
        print("-", genre)

    choice = input("\nEnter your favorite genre: ").title()

    if choice in movies:
        print("\nRecommended Movies:")
        for movie in movies[choice]:
            print("✔", movie)

        print("\n⭐ Top Pick for You:")
        print(random.choice(movies[choice]))

    else:
        print("\n❌ Genre not available.")

    again = input("\nDo you want another recommendation? (yes/no): ").lower()

    if again != "yes":
        print("\nThank you for using the Recommendation System!")
        break