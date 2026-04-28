from app.services.analyzer_service import analyze

def run():
    password = input("Enter password: ")

    result = analyze(password)

    print("\n--- Analysis Result ---")
    for key, value in result.to_dict().items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    run()
