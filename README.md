# PillDispenseBot

Welcome to PillDispenseBot – the future of personalized medication management. This project is a testament to the power of integration between hardware and software, delivering a user-friendly, secure, and efficient way to manage your medication schedule.

## Features

- **Automated Medication Dispensing**: Utilizes servo motors controlled by Arduino for precise and reliable delivery of pills.
- **RFID Security**: Ensures that only authorized users can access the medication, enhancing safety and privacy.
- **Touchscreen Interface**: Offers an intuitive and interactive way for users to manage their medication details and schedules.
- **Telegram Notifications**: Sends timely alerts and reminders to users for medication intake, ensuring adherence to prescriptions.
- **USB Connectivity**: Connects Arduino with Raspberry Pi using USB, making the setup clean and modular.
- **Python and Standard Firmata**: Leverages the versatility of Python and the convenience of Standard Firmata for seamless hardware-software communication.

## Getting Started

To get started with PillDispenseBot, clone this repository and follow the setup instructions in the documentation. Ensure you have the necessary hardware components and software dependencies installed.

## Installation

1. Set up your Raspberry Pi and connect the touchscreen.
2. Connect the Arduino to the Raspberry Pi via USB.
3. Install Standard Firmata on Arduino.
4. Install the required Python libraries for RFID, Telegram Bot, and servo motor control.
5. Configure your Telegram bot and obtain the API token.
6. Follow the wiring diagram provided to connect the servo motors and RFID reader.

## Usage

Once everything is set up, run the main script to start the PillDispenseBot. Use your RFID card to authenticate, select your medication on the touchscreen, and let the bot handle the rest. You'll receive a Telegram notification once your pills are dispensed.

## Contributing

Contributions to PillDispenseBot are welcome! Please read the contributing guidelines before submitting your pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to the Raspberry Pi Foundation for the versatile hardware.
- Gratitude to the Arduino community for the robust control solutions.
- Appreciation for the Python Software Foundation for the powerful programming language.

PillDispenseBot is more than just a project; it's a step towards a healthier future. Join us in revolutionizing medication management!

