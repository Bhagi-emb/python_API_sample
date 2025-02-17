from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import requests
import os

class TourTravellerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Tour Traveller")
        self.setGeometry(100, 100, 500, 600)

        layout = QVBoxLayout()

        # Title
        title = QLabel("Tour Traveller")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        # Destination Selection
        layout.addWidget(QLabel("Select Destination Type:"))
        self.destination_type = QComboBox()
        self.destination_type.addItems(["None", "National", "International"])
        self.destination_type.currentIndexChanged.connect(self.update_itinerary_options)
        layout.addWidget(self.destination_type)

        # Itinerary Builder
        layout.addWidget(QLabel("Select Your Itinerary:"))
        self.itinerary_options = QComboBox()
        self.itinerary_options.addItem("None")
        layout.addWidget(self.itinerary_options)

        # Cost Estimator
        layout.addWidget(QLabel("Estimated Budget ($):"))
        self.budget_entry = QLineEdit()
        layout.addWidget(self.budget_entry)

        # Booking Button
        book_button = QPushButton("Book Now")
        book_button.clicked.connect(self.book_trip)
        layout.addWidget(book_button)

        # Display Reviews Button
        reviews_button = QPushButton("View Reviews")
        reviews_button.clicked.connect(self.show_reviews)
        layout.addWidget(reviews_button)

        # Customer Support Button
        support_button = QPushButton("Contact Support")
        support_button.clicked.connect(self.contact_support)
        layout.addWidget(support_button)

        # Call API Button
        api_button = QPushButton("Generate Itinerary (AI)")
        api_button.clicked.connect(self.call_openai_api)
        layout.addWidget(api_button)

        self.setLayout(layout)
        self.update_itinerary_options()

    def update_itinerary_options(self):
        destination_type = self.destination_type.currentText()
        if destination_type == "National":
            options = ["None", "Rajasthan", "Himachal Pradesh", "Uttarakhand", "Kerala", "Goa"]
        elif destination_type == "International":
            options = ["None", "France", "Italy", "Switzerland", "United Kingdom", "Germany"]
        else:
            options = ["None"]
        
        self.itinerary_options.clear()
        self.itinerary_options.addItems(options)

    def book_trip(self):
        destination = self.destination_type.currentText()
        itinerary = self.itinerary_options.currentText()
        budget = self.budget_entry.text()

        if destination == "None" or itinerary == "None" or not budget:
            QMessageBox.critical(self, "Error", "All fields must be filled!")
            return

        QMessageBox.information(self, "Success", f"Trip to {destination} ({itinerary}) booked successfully!")

    def show_reviews(self):
        QMessageBox.information(self, "Reviews", "⭐⭐⭐⭐⭐ 'Amazing Experience!'\n⭐⭐⭐⭐ 'Great Budget Options!'")

    def contact_support(self):
        QMessageBox.information(self, "Support", "24/7 Support: Call +123-456-7890")

    def call_openai_api(self):
        try:
            api_key = os.getenv("OPENAI_API_KEY")  # Load from environment variable
            if not api_key:
                QMessageBox.critical(self, "API Error", "API key not set. Please set OPENAI_API_KEY.")
                return
            
            destination = self.destination_type.currentText()
            itinerary = self.itinerary_options.currentText()
            if destination == "None" or itinerary == "None":
                QMessageBox.critical(self, "Error", "Please select a destination and itinerary.")
                return

            prompt = f"Generate a travel itinerary for a trip to {itinerary} in {destination}."
            url = "https://api.openai.com/v1/chat/completions"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            }
            data = {
                "model": "gpt-4",
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 100
            }
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                response_data = response.json()
                itinerary = response_data.get("choices", [{}])[0].get("message", {}).get("content", "No itinerary found.")
                QMessageBox.information(self, "AI Itinerary", f"{itinerary}")
            else:
                QMessageBox.critical(self, "API Error", f"API call failed with status code: {response.status_code}")
        except Exception as e:
            QMessageBox.critical(self, "API Error", f"An error occurred: {str(e)}")

# Run the application
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = TourTravellerApp()
    window.show()
    sys.exit(app.exec_())

#command prompt i/p:
#export OPENAI_API_KEY=
#"sk-svcacct-og7zRnK94lhckFXM2tOCR_aoKGsUaXGqxW7tSoSgkUlL4gih3IUDC0yPNQHuYPbT3BlbkFJfR4i91plv_jGOAR8d84H
#_fMImOyVz7TZ7KSz9q6lWPETTCZK1yjiZBdAh1Y9X1wA"
#python sample.py
