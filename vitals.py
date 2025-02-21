class VitalSigns:
    def __init__(self, temperature, pulse, blood_pressure):
        self.temperature = temperature
        self.pulse = pulse
        self.blood_pressure = blood_pressure

    def display(self):
        print(f"Vital Signs - Temperature: {self.temperature}, Pulse: {self.pulse} bpm, Blood Pressure: {self.blood_pressure}")
