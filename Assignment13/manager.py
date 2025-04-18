from employee import Employee

class Manager(Employee):
    def __init__(self, name="", idNumber=0, department="", position="Manager"):
        super().__init__(name, idNumber, department, position)
        self.team_members = []

    # New method to add team members
    def add_team_member(self, employee_name):
        self.team_members.append(employee_name)

    # Overridden method
    def get_position(self):
        return f"Manager of {self.department}"

    # Display manager info and team
    def display_info(self):
        print("Manager Name:", self.get_name())
        print("ID Number:", self.get_idNumber())
        print("Department:", self.get_department())
        print("Position:", self.get_position())
        print("Team Members:", ", ".join(self.team_members))
        print("-" * 30)
