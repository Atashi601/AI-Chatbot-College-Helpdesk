print("🤖 College Helpdesk Chatbot Started!")
print("Type 'exit' to stop\n")

while True:
    user = input("You: ").lower()

    if user == "exit":
        print("Bot: Goodbye! Have a nice day 👋")
        break

    elif "admission" in user:
        print("Bot: Admission starts every year in June. Visit the college website for details.")

    elif "fees" in user:
        print("Bot: Fees range between 30,000 to 80,000 per year depending on course.")

    elif "course" in user or "courses" in user:
        print("Bot: We offer CSE, IT, ECE, Mechanical, Civil Engineering.")

    elif "placement" in user:
        print("Bot: Average placement is 3-6 LPA. Top companies visit every year.")

    elif "location" in user:
        print("Bot: The college is located in Kolkata, West Bengal.")

    elif "hostel" in user:
        print("Bot: Yes, hostel facilities are available for both boys and girls.")

    elif "library" in user:
        print("Bot: The college has a modern digital library with many books and journals.")

    elif "principal" in user:
        print("Bot: The principal office is available during working hours in the main campus.")

    else:
        print("Bot: Sorry, I didn't understand. Please ask about admission, fees, courses, placement, hostel, or library.")
