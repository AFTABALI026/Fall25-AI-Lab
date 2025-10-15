class ModelBasedReflexAgent:
    def __init__(self, desired_temp):
        self.fixed_temp = desired_temp
        self.current_temp = None
        self.previous_action = None

    def sensor(self, temp):
        self.current_temp = temp

    def performance(self):
        if self.current_temp is None:
            return "No temperature data"

        if self.current_temp > self.fixed_temp:
            action = "Turn on the AC"
        elif self.current_temp < self.fixed_temp:
            action = "Turn on the Heater"
        else:
            action = "Already Optimal"

        if action == self.previous_action:
            return "No change (already performing same action)"
        
        self.previous_action = action
        return action

    def actuator(self):
        action = self.performance()
        print(f"Room Temp: {self.current_temp}°C | Action: {action}")


# Example test
agent = ModelBasedReflexAgent(desired_temp=22)
temps = [20, 23, 23, 22, 21]

for t in temps:
    agent.sensor(t)
    agent.actuator()
